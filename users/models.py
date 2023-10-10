from django.db import models


# Создаем модель базы данных для таблицы Кастомных Пользователей
class CustomUser(models.Model):
    username = models.CharField(max_length=54, unique=True)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
