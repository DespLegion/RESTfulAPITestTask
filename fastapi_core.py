from fastapi import FastAPI

from mysite import settings

from jwt_auth.endpoints import auth_router
from ore_concentration.endpoints import ore_router
from views import view_router

# Отдельно создаем описание проекта FastAPI для удобства редактирования
description = """
FastAPI + Django ORM Test Task.
"""

# Инициализируем приложение FastAPI и применяем к нему первичные настройки
app = FastAPI(
    title="RESTful API Test Task",
    description=description,
    openapi_url=f"/api/openapi.json",
    version="0.0.1",
    debug=settings.DEBUG,
)

# Подключаем к приложение роутер эндпоинтов, связанных с авторизацией
app.include_router(auth_router, tags=['Auth'], prefix="/api")

# Подключаем к приложение роутер эндпоинтов, связанных с записями о концентрации руд и Шахтами
app.include_router(ore_router, tags=['Ore concentration'], prefix="/api")

# Подключаем к приложению роутер для отображения HTML Frontend`а
app.include_router(view_router, tags=['Views'])
