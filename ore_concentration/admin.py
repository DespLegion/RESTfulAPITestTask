from django.contrib import admin
from .models import Mine, OreConcentration


# Регистрируем модель Шахт в Django Admin для возможности
# их отслеживания и добавления через интерфейс Django Admin
@admin.register(Mine)
class MineAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


# Регистрируем модель записей о концентрации руд в Django Admin для возможности
# их отслеживания и добавления через интерфейс Django Admin
@admin.register(OreConcentration)
class OreConcentrationAdmin(admin.ModelAdmin):
    list_display = (
        'mine_name',
        'concentration_date',
        'iron_concentration',
        'silicon_concentration',
        'aluminum_concentration',
        'calcium_concentration',
        'sulfur_concentration',
    )
    list_filter = (
        'mine_name',
        'concentration_date',
        'iron_concentration',
        'silicon_concentration',
        'aluminum_concentration',
        'calcium_concentration',
        'sulfur_concentration',
    )
    search_fields = ('mine_name', 'concentration_date')

