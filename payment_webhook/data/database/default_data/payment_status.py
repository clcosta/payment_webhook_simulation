from sqlalchemy.engine import Engine
from sqlmodel import Session

from payment_webhook.data.contracts import PaymentStatus

from ..models import PaymentType


def create_payments_data(engine: Engine):
    data = [PaymentType(status=sts.value) for sts in list(PaymentStatus)]
    with Session(engine) as s:
        s.add_all(data)
        s.commit()
