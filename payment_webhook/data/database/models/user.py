from datetime import datetime

from sqlmodel import Field

from payment_webhook.data.contracts import IUser


class User(IUser, table=True):  # Table and Schema
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    access_aproved: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    deleted_at: datetime | None = Field(default=None)
