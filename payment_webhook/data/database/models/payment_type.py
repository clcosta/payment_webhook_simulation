from sqlalchemy import Column, Integer, String

from .base import BaseModel


class PaymentTypeModel(BaseModel):
    __tablename__ = 'payment_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(20))

    def __repr__(self) -> str:
        return 'UserModel(status={!r})'.format(self.status)
