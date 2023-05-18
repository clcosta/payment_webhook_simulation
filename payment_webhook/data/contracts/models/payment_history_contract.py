from sqlmodel import SQLModel


class IPaymentHistory(SQLModel):   # Schema not database
    user_email: str
    payment_type_id: int
