from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from jwt_auth.auth import pwd_context, create_jwt_token
from jwt_auth.schemas import Token, RegisterResponse

from users.models import CustomUser
from users.schemas import User


# Создаем общий роутер дл эндпоинтов авторизации
auth_router = APIRouter()


# Эндпоинт для авторизации пользователей
@auth_router.post('/login', response_model=Token)
def login(user: User):
    # Проверяем есть ли пользователь с таким логином(юзернеймом) в БД
    if not CustomUser.objects.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Если юзер с таким логином есть, получаем его из БД
    db_user = CustomUser.objects.get(username=user.username)
    # Проверяем соответствует ли веденных пользователем пароль, хешированному паролю из БД
    is_password_correct = pwd_context.verify(user.password, db_user.password)

    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Если логин и пароль соответствую данным в БД - создаем новый JWT токен и передаем его пользователю
    jwt_token = create_jwt_token({"sub": user.username})
    return JSONResponse(status_code=200, content={"access_token": jwt_token, "token_type": "bearer"})


# Эндпоинт для регистрации новых пользователей
@auth_router.post('/register', response_model=RegisterResponse)
def register(user: User):
    # Сразу хешируем пароль, полученный от пользователя
    hashed_password = pwd_context.hash(user.password)

    # Проверяем на наличие пользователя с таким-же логином в БД
    if CustomUser.objects.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail=f"User with such name ({user.username}) already exists")

    # Если пользователя с таким логином в БД нет, пытаемся создать нового пользователя и сохранить его в БД
    try:
        new_user = CustomUser()
        new_user.username = user.username
        new_user.password = hashed_password
        new_user.save()
        # В случае успеха возвращаем JSON с ID пользователя и сообщением об успешной регистрации
        return JSONResponse(status_code=200, content={"status": "success", "id": new_user.id, "success": True})
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error - {err}")
