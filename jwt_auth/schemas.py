from pydantic import BaseModel


# Pydantic модель для ответа при запросе токена
class Token(BaseModel):
    access_token: str
    token_type: str


# Модель для ответа после успешной регистрации пользователя
class RegisterResponse(BaseModel):
    status: str
    id: int
    success: bool
