from django.contrib import admin
from .models import CustomUser


# Регистрируем модель Кастомных Пользователей в Django Admin для возможности
# их отслеживания и добавления через интерфейс Django Admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)
