import os
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

# Получаем переменных окружения из .env файла, для их дальнейшего использования в приложении

# Global DEBUG mode
ENV_DEBUG = os.getenv('DEBUG')

# DB connection settings
ENV_DB_NAME = os.getenv('DB_NAME')
ENV_DB_USER = os.getenv('DB_USER')
ENV_DB_PASSWORD = os.getenv('DB_PASSWORD')
ENV_DB_HOST = os.getenv('DB_HOST')
ENV_DB_PORT = os.getenv('DB_PORT')

# JWT Auth settings
ENV_AUTH_COOKIE_NAME = os.getenv('AUTH_COOKIE_NAME')
ENV_AUTH_ALGORITHM = os.getenv('AUTH_ALGORITHM')
ENV_AUTH_TOKEN_EXPIRATION_TIME = os.getenv('AUTH_TOKEN_EXPIRATION_TIME')
ENV_AUTH_SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
