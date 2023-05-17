from sqlmodel import Session
from sqlalchemy.engine import Engine
from payment_webhook.data.service import PaymentStatus
from ..models import PaymentType


def create_payments_data(engine: Engine):
    data = [PaymentType(status=sts.value) for sts in list(PaymentStatus)]
    with Session(engine) as s:
        s.add_all(data)
        s.commit()
