from sqlmodel import create_engine

from payment_webhook.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
