from typing import Any, Type

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, SQLModel, select, text

from payment_webhook.data.contracts import (
    IPaymentHistory,
    IUser,
    PaymentStatus,
)
from payment_webhook.settings import BASE_PATH

from .default_data import create_payments_data
from .engine import engine
from .models import PaymentHistory, PaymentType, User


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class DataBase:

    _session: Session = None
    autocommit = True
    User = User
    PaymentType = PaymentType
    PaymentHistory = PaymentHistory

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

    def __get(self, model: Type[SQLModel], **kwargs: dict) -> Any:
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

    def register_payment(self, **kwargs: IPaymentHistory):
        instance = self.PaymentHistory(**kwargs)
        self.__add(instance)

    def register_user(self, **kwargs: IUser) -> User:
        instance = self.User(**kwargs)
        self.__add(instance)
        return instance

    def get_user(
        self, id: int | None = None, email: str | None = None
    ) -> User:
        if not any([id, email]):
            raise ValueError('id or email are required')
        if id:
            return self.__get(DataBase.User, id=id)
        return self.__get(DataBase.User, email=email)

    def aprove_user_access(self, user_id: int) -> User:
        user = self.get_user(id=user_id)
        user.access_aproved = True
        self._session.refresh(user)
        return user

    def revoke_user_access(self, user_id: int) -> User:
        user = self.get_user(id=user_id)
        user.access_aproved = False
        self._session.refresh(user)
        return user


# LOCAL
db_path = BASE_PATH.parent / 'db.db'
if not db_path.exists():
    create_db_and_tables()
    create_payments_data(engine)
