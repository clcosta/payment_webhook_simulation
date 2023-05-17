from sqlmodel import SQLModel

class IPaymentHistory(SQLModel): # Schema not database
    user_id: int
    payment_type_id: int
