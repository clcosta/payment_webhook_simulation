from pydantic import BaseModel


class PaymentTypeSchema(BaseModel):   # Schema not database
    status: str
