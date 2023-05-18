from sqlalchemy.orm import declared_attr
from sqlmodel import Field

from payment_webhook.data.contracts import IPaymentType


class PaymentType(IPaymentType, table=True):   # Table and Schema
    id: int | None = Field(default=None, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return 'payment_type'
