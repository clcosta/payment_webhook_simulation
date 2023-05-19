from payment_webhook.data.contracts import Actions, PaymentStatus
from payment_webhook.data.database import DataBase

from .webhook_schemas import WebhookBodySchema


class PaymentHandle:
    data: WebhookBodySchema = None

    def __register_payment(self, actions: list[Actions]) -> DataBase.User:
        with DataBase() as db:
            user = db.get_user(email=self.data.email)
            if not user:
                user = db.add_user(nome=self.data.nome, email=self.data.email)
            payment_type_id = db.get_payment_type_id(
                payment_type=self.data.status
            )
            db.register_payment(
                user_email=user.email,
                payment_type_id=payment_type_id,
                actions=actions,
            )
        return user

    def _payment_approved(self):
        actions = [Actions.ACCESS_APPROVED, Actions.SEND_MESSAGE]
        user = self.__register_payment(actions=actions)
        with DataBase() as db:
            db.aprove_user_access(user_id=user.id)
        # SEND MESSAGE TO EMAIL
        print(
            f'Usuário {user.nome}({user.email}): Pagamento aprovado e acesso liberado!'
        )

    def _payment_refused(self):
        actions = [Actions.SEND_MESSAGE]
        user = self.__register_payment(actions=actions)
        # SEND MESSAGE TO EMAIL
        print(f'Usuário {user.nome}({user.email}): Pagamento foi recusado!')

    def _payment_refunded(self):
        actions = [Actions.REVOKE_ACCESS, Actions.SEND_MESSAGE]
        user = self.__register_payment(actions=actions)
        with DataBase() as db:
            db.revoke_user_access(user_id=user.id)
        # SEND MESSAGE TO EMAIL
        print(f'Usuário {user.nome}({user.email}): Pagamento foi reembolsado!')

    def process(self, body: dict) -> PaymentStatus:
        self.data = WebhookBodySchema(**body)

        match self.data.status:
            case PaymentStatus.APPROVED:
                self._payment_approved()
                return PaymentStatus.APPROVED
            case PaymentStatus.REFUSED:
                self._payment_refused()
                return PaymentStatus.REFUSED
            case PaymentStatus.REFUNDED:
                self._payment_refunded()
                return PaymentStatus.REFUNDED
            case _:
                raise RuntimeError(
                    'Panic: Something went wrong on payment process'
                )
