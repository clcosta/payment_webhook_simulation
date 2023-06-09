from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseModel
from .payment_type import PaymentTypeModel


class PaymentHistoryModel(BaseModel):
    __tablename__ = 'payment_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    payment_type_id = Column(Integer, ForeignKey(PaymentTypeModel.id))
    payment_type = relationship(
        'PaymentTypeModel', backref='parent_type', lazy='subquery'
    )
    info = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
