from pydantic import BaseModel


# Модель pydantic для валидации входящих данных при регистрации и авторизации пользователей
class User(BaseModel):
    username: str
    password: str
