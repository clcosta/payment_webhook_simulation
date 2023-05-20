from pydantic import BaseModel


class PaymentHistorySchema(BaseModel):   # Schema not database
    user_email: str
    payment_type_id: int
    info: dict | str
