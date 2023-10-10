# Generated by Django 4.2.6 on 2023-10-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54, unique=True, verbose_name='Название шахты')),
            ],
            options={
                'verbose_name': 'Mine',
                'verbose_name_plural': 'Mines',
            },
        ),
        migrations.CreateModel(
            name='OreConcentration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iron_concentration', models.FloatField(max_length=20, verbose_name='Концентрация железа')),
                ('silicon_concentration', models.FloatField(max_length=20, verbose_name='Концентрация кремния')),
                ('aluminum_concentration', models.FloatField(max_length=20, verbose_name='Концентрация алюминия')),
                ('calcium_concentration', models.FloatField(max_length=20, verbose_name='Концентрация кальция')),
                ('sulfur_concentration', models.FloatField(max_length=20, verbose_name='Концентрация серы')),
                ('concentration_date', models.DateField(verbose_name='Дата')),
                ('mine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ore_concentration.mine', verbose_name='Наименование шахты')),
            ],
            options={
                'verbose_name': 'Ore concentration',
                'verbose_name_plural': 'Ore concentrations',
            },
        ),
    ]
