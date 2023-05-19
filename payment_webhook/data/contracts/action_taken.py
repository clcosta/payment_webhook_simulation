from enum import Enum


class Actions(Enum):
    SEND_MESSAGE = 'Mensagem enviada ao usuário'
    ACCESS_APPROVED = 'Acesso ao curso aprovado'
    REVOKE_ACCESS = 'Acesso ao curso removido'
