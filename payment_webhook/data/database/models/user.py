from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .base import BaseModel


class UserModel(UserMixin, BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(50), unique=True)
    access_aproved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return 'UserModel(nome={!r}, email={!r})'.format(self.nome, self.email)
