from enum import Enum

class PaymentStatus(Enum):
    APPROVED = 'aprovado'
    REFUSED = 'reprovado'
    REFUNDED = 'reembolso'