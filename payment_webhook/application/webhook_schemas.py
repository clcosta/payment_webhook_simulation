from pydantic import BaseModel

from payment_webhook.data.contracts import PaymentStatus


class WebhookBodySchema(BaseModel):

    nome: str
    email: str
    status: PaymentStatus
    valor: int
    forma_pagamento: str
    parcelas: int
