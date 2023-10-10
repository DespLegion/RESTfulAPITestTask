from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from jwt_auth.auth import get_current_user
from users.schemas import User


# Создаем роутер для эндпоинтов отображения HTML шаблонов
view_router = APIRouter()

# Регистрируем директорию шаблонов
templates = Jinja2Templates(directory="static/templates")


# Эндпоинт для отображения шаблона авторизации
@view_router.get('/login', response_class=HTMLResponse)
def view_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Эндпоинт для отображения шаблона получения записей о концентрации руд
# эндпоинт закрыт для неавторизованных пользователей
@view_router.get('/ore_stats', response_class=HTMLResponse)
def view_ore_stats(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("ore.html", {"request": request})


# Эндпоинт для отображения шаблона для создания новой записи о концентрации руд
# эндпоинт закрыт для неавторизованных пользователей
@view_router.get('/create_note', response_class=HTMLResponse)
def view_create_note(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("create_ore_note.html", {"request": request})
