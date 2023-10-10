# Generated by Django 4.2.6 on 2023-10-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ore_concentration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oreconcentration',
            name='aluminum_concentration',
            field=models.FloatField(max_length=20, verbose_name='Концентрация алюминия %'),
        ),
        migrations.AlterField(
            model_name='oreconcentration',
            name='calcium_concentration',
            field=models.FloatField(max_length=20, verbose_name='Концентрация кальция %'),
        ),
        migrations.AlterField(
            model_name='oreconcentration',
            name='concentration_date',
            field=models.DateField(help_text='Format: <em>YYYY-MM-DD</em>.', verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='oreconcentration',
            name='iron_concentration',
            field=models.FloatField(max_length=20, verbose_name='Концентрация железа %'),
        ),
        migrations.AlterField(
            model_name='oreconcentration',
            name='silicon_concentration',
            field=models.FloatField(max_length=20, verbose_name='Концентрация кремния %'),
        ),
        migrations.AlterField(
            model_name='oreconcentration',
            name='sulfur_concentration',
            field=models.FloatField(max_length=20, verbose_name='Концентрация серы %'),
        ),
    ]
