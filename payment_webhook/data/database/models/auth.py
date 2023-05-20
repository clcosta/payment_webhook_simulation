from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from werkzeug.security import check_password_hash

from .base import BaseModel


class AuthModel(BaseModel):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True)
    password = Column(String(100))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)

    def validate_password(self, plain_password: str) -> bool:
        return check_password_hash(self.password, plain_password)

    def __repr__(self) -> str:
        return 'AuthModel(email={!r}, password={!r})'.format(
            self.email, self.password
        )
