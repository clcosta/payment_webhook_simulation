from sqlmodel import SQLModel


class IPaymentType(SQLModel):   # Schema not database
    status: str
