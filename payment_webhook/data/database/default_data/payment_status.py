from payment_webhook.data.contracts import PaymentStatus, PaymentTypeSchema


def get_payment_status_values() -> list[PaymentTypeSchema]:
    data = [PaymentTypeSchema(status=sts.value) for sts in list(PaymentStatus)]
    return data
