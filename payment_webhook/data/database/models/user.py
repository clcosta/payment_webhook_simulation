from payment_webhook.data.contracts import IUser
from sqlmodel import Field


class User(IUser, table=True):  # Table and Schema
    id: int | None = Field(default=None, primary_key=True)

