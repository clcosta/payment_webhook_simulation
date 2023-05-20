from sqlalchemy.orm import sessionmaker

from payment_webhook.infra.settings import BASE_PATH

from .context import DataBaseContext
from .default_data import get_payment_status_values
from .engine import engine
from .models import BaseModel, PaymentTypeModel


class DataBase:
    __Session = sessionmaker(bind=engine)
    engine = engine

    def __enter__(self):
        self.conn = self.engine.connect()
        self.__context = DataBaseContext(
            session=self.__Session, conn=self.conn
        )
        self.__create_tables()
        self.__insert_default_values()
        return self.__context

    def __exit__(self, *args):
        self.__context.close()

    def __create_tables(self):
        BaseModel.metadata.create_all(self.engine)

    def __insert_default_values(self):
        payment_status = get_payment_status_values()
        payment_status = [
            PaymentTypeModel(status=p.status) for p in payment_status
        ]
        payments_status = self.__context.get_all_payment_status()
        if not payments_status:
            self.__context.add_all(payment_status)
            self.__context.commit()
