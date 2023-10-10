from typing import Optional

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param

from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

import config


# Немного измененный стандартный класс FastAPI OAuth2PasswordBearer
# Добавлен дополнительный источник получения токена авторизации
# По умолчанию токен получается только из заголовка запроса
# В нашем случае токен хранится в Куки файлах клиента, если клиент использует фронтенд часть приложения, а не голые API
# В таком случае получать его нужно из Куки, а не из заголовка
# Но если клиент использует голые API, то токен по прежнему нужно получать из заголовка
class OAuth2PasswordBearerByCookie(OAuth2PasswordBearer):

    async def __call__(self, request: Request) -> Optional[str]:
        # Тут мы пытаемся получить токен из заголовка запроса
        authorization = request.headers.get("Authorization")
        # Если в заголовке токена нет, пытаемся получить из Куки файлов клиента
        if not authorization:
            authorization: str = request.cookies.get(config.ENV_AUTH_COOKIE_NAME)
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param
