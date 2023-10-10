import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from fastapi import Depends, HTTPException

from jwt_auth.utils import OAuth2PasswordBearerByCookie
from users.models import CustomUser

import config

SECRET_KEY = config.ENV_AUTH_COOKIE_NAME
ALGORITHM = config.ENV_AUTH_ALGORITHM
EXPIRATION_TIME = timedelta(minutes=int(config.ENV_AUTH_TOKEN_EXPIRATION_TIME))

oauth2_scheme = OAuth2PasswordBearerByCookie(tokenUrl="/api/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Создание JWT токена с заданными параметрами
def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


# Проверка токена на валидность и его декодирование
def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


# Если токен валиден - получаем юзера по декодированным данным из базы данных
def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded_data = verify_jwt_token(token)

    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")

    if not CustomUser.objects.filter(username=decoded_data["sub"]).exists():
        raise HTTPException(status_code=400, detail="User not found")

    user = CustomUser.objects.get(username=decoded_data["sub"])
    return user
