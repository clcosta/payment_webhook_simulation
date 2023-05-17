## CONFIG FILE TO APPLICATION
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# BASE URL

BASE_PATH = Path(__file__).parent

# DATABASE
DATABASE_URL = 'sqlite:///db.db'

# TEMPLATE_DIR
TEMPLATE_DIR = BASE_PATH / 'main/server/templates'

# ENCRYPTION
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', default='YOUR-SECRET-KEY-OF-ENCRYPTION')