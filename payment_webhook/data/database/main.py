import json
from typing import Any, Type, TypeVar

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, SQLModel, select, text

from payment_webhook.data.contracts import Actions, PaymentStatus
from payment_webhook.settings import BASE_PATH

from .default_data import create_payments_data
from .engine import engine
from .models import Auth, PaymentHistory, PaymentType, User

Repository = TypeVar('Repository')


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class DataBase:
    _session: Session = None
    autocommit = True
    User = User
    PaymentType = PaymentType
    PaymentHistory = PaymentHistory
    Auth = Auth

    def __enter__(self):
        self._session = Session(bind=engine)
        return self

    def __exit__(self, *args, **kwargs):
        self._session.close()

    def __add(self, instance: Any, **kwargs):
        try:
            self._session.add(instance, **kwargs)
            if self.autocommit:
                self._session.commit()
                self._session.refresh(instance)
        except IntegrityError as er:
            self._session.rollback()
            raise er
        except Exception as er:
            print(er)
            raise er

    def __get(
        self, model: Repository, **kwargs
    ) -> Repository | None | list[Repository]:
        if kwargs:
            filter_args = [
                text(k + ' == ' + repr(v)) for k, v in kwargs.items()
            ]
            return self._session.exec(
                select(model).where(*filter_args)
            ).first()
        return self._session.exec(select(model)).all()

    def get_payment_type_id(self, payment_type: PaymentStatus | str) -> int:
        _type = PaymentStatus(payment_type)
        result = self.__get(DataBase.PaymentType, status=_type.value)
        return result.id

    def register_payment(self, actions: list[Actions] = None, **kwargs):
        if not actions and 'actions' not in kwargs:
            raise ValueError('actions are required')
        elif not actions and 'actions' in kwargs:
            actions = kwargs.pop('actions')
        actions = [action.value for action in actions]
        data = {
            'actionsTaken': actions,
            'valor': kwargs.get('valor', 0),
            'formaDePagamento': kwargs.get(
                'forma_de_pagamento', 'Não informado'
            ),
            'parcelas': kwargs.get('parcelas', 1),
        }
        kwargs['info'] = json.dumps(data)
        instance = self.PaymentHistory(**kwargs)
        if isinstance(instance.info, dict):
            instance.info = json.dumps(instance.info)
        self.__add(instance)

    def register_user(self, **kwargs) -> User:
        auth_instance = self.Auth(**kwargs)
        self.__add(auth_instance)
        user_name = auth_instance.email.split('@')[0]
        user_instance = self.add_user(
            nome=user_name, email=auth_instance.email
        )
        return user_instance

    # noinspection PyArgumentList
    def get_registered_user(
        self, email: str, password: str
    ) -> Type[User] | None:
        user_auth = self.__get(DataBase.Auth, email=email)
        if not user_auth:
            return None
        # noinspection PyArgumentList
        if user_auth.verify_password(password=password):
            user = self.__get(DataBase.User, email=user_auth.email)
            if user:
                return user
            else:
                raise ValueError('User are not registered')
        raise ValueError('Password mismatch')

    def add_user(self, **kwargs) -> User:
        instance = self.User(**kwargs)
        self.__add(instance)
        return instance

    def get_user(
        self, user_id: int | None = None, email: str | None = None
    ) -> Type[User] | None:
        if not any([user_id, email]):
            raise ValueError('id or email are required')
        if user_id:
            return self.__get(DataBase.User, id=user_id)
        return self.__get(DataBase.User, email=email)

    def aprove_user_access(self, user_id: int) -> Type[User]:
        user = self.get_user(user_id=user_id)
        user.access_aproved = True
        self._session.commit()
        self._session.refresh(user)
        return user

    def revoke_user_access(self, user_id: int) -> Type[User]:
        user = self.get_user(user_id=user_id)
        user.access_aproved = False
        self._session.commit()
        self._session.refresh(user)
        return user


# LOCAL
db_path = BASE_PATH.parent / 'db.db'
if not db_path.exists():
    create_db_and_tables()
    create_payments_data(engine)
