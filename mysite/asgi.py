"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django

from django.core.wsgi import get_wsgi_application
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware


from fastapi.staticfiles import StaticFiles

from mysite import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
# Инициализируем джанго как WSGI прилоежние
application = get_wsgi_application()


# Импортируем приложение FastAPI
from fastapi_core import app


fastapiapp = app


# Собираем комплексное приложение (FastAPI + Django WSGI)
def create_application(fastapp):
    # Применяем настройки к FastAPI приложениею
    fastapp.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.ALLOWED_HOSTS] or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Монтируем в приложение FastAPI WSGI приложение Django
    fastapp.mount(f"/django", WSGIMiddleware(application))
    # Монтируем в приложение FastAPI директорию для статических данных
    # для использования в Django Admin и для обработки шаблонов
    fastapp.mount("/static", StaticFiles(directory="static"), name="static")

    return fastapp


# Вызываем, созданный выше, конструктор комплексного приложения
# comp_app является главной точкой входа для uvicorn
comp_app = create_application(fastapiapp)
