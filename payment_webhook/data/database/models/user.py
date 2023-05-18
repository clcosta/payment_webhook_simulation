from sqlalchemy import Unicode
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import Column, Field

from payment_webhook.data.contracts import IUser
from payment_webhook.settings import ENCRYPTION_KEY


class User(IUser, table=True):  # Table and Schema
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    access_aproved: bool = Field(default=False)
    password: str = Field(
        sa_column=Column(
            EncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, 'pkcs5')
        )
    )

    def check_pwd_equals(self, password: str) -> bool:
        return self.password == password
