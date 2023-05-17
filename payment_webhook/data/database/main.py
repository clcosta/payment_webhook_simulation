from payment_webhook.settings import BASE_PATH
from sqlmodel import SQLModel, Session
from .engine import engine
from .models import User, PaymentType, PaymentHistory
from typing import Any
from .default_data import create_payments_data

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

class DataBase:

    _session: Session = None
    autocommit = True
    user = User
    payment_type = PaymentType
    payment_history = PaymentHistory

    def __enter__(self):
        self._session = Session(bind=engine)
        return self

    def __exit__(self, *args, **kwargs):
        self._session.close()

    def add(self, instance: Any, **kwargs) -> None:
        self._session.add(instance, **kwargs)
        if self.autocommit:
            self._session.commit()
            self._session.refresh(instance)


# LOCAL
db_path = BASE_PATH.parent / 'db.db'
if not db_path.exists():
    create_db_and_tables()
    create_payments_data(engine)

user = DataBase.user(email='abc@abc.com',password='password')
with DataBase() as db:
    db.add(user)
    print(user)