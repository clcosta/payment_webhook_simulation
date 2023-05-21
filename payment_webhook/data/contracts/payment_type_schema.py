from pydantic import BaseModel


class PaymentTypeSchema(BaseModel):
    status: str
