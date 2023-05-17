from payment_webhook.settings import DATABASE_URL
from sqlmodel import create_engine

engine = create_engine(DATABASE_URL)
