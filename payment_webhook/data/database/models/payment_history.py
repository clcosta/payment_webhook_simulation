from datetime import datetime

from sqlalchemy.orm import declared_attr
from sqlmodel import Field

from payment_webhook.data.contracts import IPaymentHistory


class PaymentHistory(IPaymentHistory, table=True):   # Table and Schema
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id', nullable=False)
    payment_type_id: int = Field(foreign_key='payment_type.id', nullable=False)
    created_at: datetime | None = Field(default=datetime.now, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        return 'payment_history'
