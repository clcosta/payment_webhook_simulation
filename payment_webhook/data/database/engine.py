from sqlalchemy import create_engine

from payment_webhook.infra.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
