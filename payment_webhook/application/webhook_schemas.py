from pydantic import BaseModel

from payment_webhook.data.contracts import PaymentStatus


class WebhookBodyModel(BaseModel):

    nome: str
    email: str
    status: PaymentStatus
    valor: int
    forma_pagamento: str
    parcelas: int
