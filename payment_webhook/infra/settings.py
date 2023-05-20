## CONFIG FILE TO APPLICATION
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# BASE URL

BASE_PATH = Path(__file__).parent.parent.parent

# DATABASE
DATABASE_URL = 'sqlite:///db.db?check_same_thread=False'

# TEMPLATE_DIR
TEMPLATE_DIR = BASE_PATH / 'payment_webhook/main/server/templates'

# ENCRYPTION
ENCRYPTION_KEY = os.getenv(
    'ENCRYPTION_KEY', default='YOUR-SECRET-KEY-OF-ENCRYPTION'
)

# DEFAULT_ACESS_TOKEN
DEFAULT_REGISTER_TOKEN = os.getenv(
    'DEFAULT_REGISTER_TOKEN', default='uhdfaAADF123'
)
