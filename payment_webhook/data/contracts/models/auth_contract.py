from sqlmodel import SQLModel

from payment_webhook.settings import DEFAULT_REGISTER_TOKEN


class IAuthUser(SQLModel):
    email: str
    password: str
    register_token: str = DEFAULT_REGISTER_TOKEN
