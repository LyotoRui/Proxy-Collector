from datetime import timedelta
from dotenv import load_dotenv
import os


load_dotenv()

# Base settings
TESTING = True
SECRET_KEY = os.getenv("SECRET_KEY")

# Session settings
SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_PATH = None
PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
SESSION_REFRESH_EACH_REQUEST = False

