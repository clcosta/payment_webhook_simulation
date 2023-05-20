from pydantic import BaseModel

from payment_webhook.infra.settings import DEFAULT_REGISTER_TOKEN


class AuthUserSchema(BaseModel):
    email: str
    password: str
    register_token: str = DEFAULT_REGISTER_TOKEN
