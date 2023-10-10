from django.db import models


# Создаем модель базы данных для таблицы с Шахтами
class Mine(models.Model):
    name = models.CharField(max_length=54, unique=True, verbose_name='Название шахты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mine"
        verbose_name_plural = "Mines"


# Создаем модель базы данных для таблицы с записями о концентрации руд
class OreConcentration(models.Model):
    # mine_name - это внешний ключ на таблицу Mine (с шахтами)
    mine_name = models.ForeignKey('Mine', on_delete=models.CASCADE, verbose_name='Наименование шахты')
    iron_concentration = models.FloatField(max_length=20, verbose_name='Концентрация железа %')
    silicon_concentration = models.FloatField(max_length=20, verbose_name='Концентрация кремния %')
    aluminum_concentration = models.FloatField(max_length=20, verbose_name='Концентрация алюминия %')
    calcium_concentration = models.FloatField(max_length=20, verbose_name='Концентрация кальция %')
    sulfur_concentration = models.FloatField(max_length=20, verbose_name='Концентрация серы %')
    concentration_date = models.DateField(verbose_name='Дата', help_text="Format: <em>YYYY-MM-DD</em>.")

    def __str__(self):
        return f"{self.mine_name} - {self.concentration_date}"

    class Meta:
        verbose_name = "Ore concentration"
        verbose_name_plural = "Ore concentrations"
