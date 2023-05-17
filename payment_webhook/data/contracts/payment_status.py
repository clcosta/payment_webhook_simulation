from enum import Enum


class PaymentStatus(Enum):
    APPROVED = 'aprovado'
    REFUSED = 'recusado'
    REFUNDED = 'reembolsado'
