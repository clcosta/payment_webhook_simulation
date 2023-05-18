from datetime import datetime

from sqlalchemy import Unicode
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import Column, Field

from payment_webhook.data.contracts import IAuthUser
from payment_webhook.settings import ENCRYPTION_KEY


class Auth(IAuthUser, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    password: str = Field(
        sa_column=Column(
            EncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, 'pkcs5')
        )
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    deleted_at: datetime | None = Field(default=None)

    def verify_password(self, password: str) -> bool:
        return self.password == password
