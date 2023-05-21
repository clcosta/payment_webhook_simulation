from payment_webhook.data.contracts import PaymentStatus
from payment_webhook.data.database.models import PaymentTypeModel


def get_payment_status_values() -> list[PaymentTypeModel]:
    data = [PaymentTypeModel(status=sts.value) for sts in list(PaymentStatus)]
    return data
