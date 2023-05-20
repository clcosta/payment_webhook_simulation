import json
from datetime import datetime
from typing import Type

from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import Query, Session, sessionmaker
from werkzeug.security import generate_password_hash

from .. import Actions
from ..contracts import PaymentStatus
from .models import AuthModel, PaymentHistoryModel, PaymentTypeModel, UserModel
from .utils import autocommit_check


class DataBaseContext:
    autocommit = True
    User = UserModel
    Auth = AuthModel
    PaymentType = PaymentTypeModel
    PaymentHistory = PaymentHistoryModel

    def __init__(self, session: sessionmaker, conn: Connection):
        self.session: Session = session()
        self.conn = conn

    def __enter__(self) -> Connection:
        return self.conn

    def __exit__(self, *args) -> None:
        self.session.close()

    @autocommit_check
    def add(self, *args, **kwargs):
        return self.session.add(*args, **kwargs)

    @autocommit_check
    def add_all(self, *args, **kwargs):
        return self.session.add_all(*args, **kwargs)

    def commit(self):
        return self.session.commit()

    def close(self):
        self.session.close()
        self.conn.close()

    @property
    def user(self) -> Query:
        return self.session.query(UserModel)

    @property
    def payment_history(self) -> Query:
        return self.session.query(PaymentHistoryModel)

    @property
    def payment_type(self) -> Query:
        return self.session.query(PaymentTypeModel)

    @property
    def auth(self) -> Query:
        return self.session.query(AuthModel)

    def get_payment_type_id(
        self, payment_type: PaymentStatus | str
    ) -> int | None:
        payment_type = (
            payment_type
            if not isinstance(payment_type, PaymentStatus)
            else payment_type.value
        )
        res = self.payment_type.filter_by(status=payment_type).first()
        if res:
            return res.id
        return None

    def register_payment(self, actions: list[Actions], **kwargs):
        actions = [ac.value for ac in actions]
        data = {
            'actionsTaken': actions,
            'valor': kwargs.pop('valor', 0),
            'formaDePagamento': kwargs.pop(
                'forma_de_pagamento', 'Não informado'
            ),
            'parcelas': kwargs.pop('parcelas', 1),
        }
        kwargs['info'] = json.dumps(data)
        payment = self.PaymentHistory(**kwargs)
        self.add(payment)

    def register_user(self, email: str, password: str) -> User:
        auth_user = self.Auth(
            email=email, password=generate_password_hash(password)
        )
        self.add(auth_user)
        user_name = auth_user.email.split('@')[0]
        # CHECK IF THE USER ALREADY EXISTS IN SYSTEM
        user = self.user.filter_by(email=email).first()
        if user:
            return user
        user_instance = self.User(nome=user_name, email=auth_user.email)
        self.add(user_instance)
        return user_instance

    def exists_user(self, email: str) -> bool:
        auth_user = self.auth.filter_by(email=email).first()
        user = self.user.filter_by(email=email).first()
        if auth_user and user:
            return True
        return False

    def aprove_user_access(self, user_id: int) -> Type[User]:
        user = self.user.filter_by(id=user_id).first()
        user.access_aproved = True
        user.updated_at = datetime.now()
        self.commit()
        return user

    def revoke_user_access(self, user_id: int) -> Type[User]:
        user = self.user.filter_by(id=user_id).first()
        user.access_aproved = False
        user.updated_at = datetime.now()
        self.commit()
        return user

    def add_user(self, **kwargs) -> User:
        name = kwargs.pop('nome')
        email = kwargs.pop('email')
        user = self.User(nome=name, email=email)
        self.add(user)
        return user

    def get_user(
        self, user_id: int | None = None, email: str | None = None
    ) -> Type[User] | None:
        if not any([user_id, email]):
            raise ValueError('ID or Email are required')
        if user_id:
            return self.user.filter_by(id=user_id).first()
        return self.user.filter_by(email=email).first()

    def user_payment_history(self, user_id: int) -> list[Type[PaymentHistory]]:
        user = self.user.filter_by(id=user_id).first()
        result = self.payment_history.filter_by(email=user.email).all()
        return result

    def get_registered_user(
        self, email: str, password: str
    ) -> Type[User] | None:
        auth_user = self.auth.filter_by(email=email).first()
        user = self.user.filter_by(email=email).first()
        if not auth_user and not user:
            return None
        elif not auth_user and user:
            raise ValueError(
                'Sua credenciais nunca foram criadas, por favor crie-as na página de registro.'
            )
        if auth_user.validate_password(plain_password=password):
            if user:
                return user
            else:
                raise ValueError('Usuário não foi registrado corretamente!')
        raise ValueError('A senha está incorreta')

    def get_all_payment_status(self) -> list:
        return self.payment_type.all()
