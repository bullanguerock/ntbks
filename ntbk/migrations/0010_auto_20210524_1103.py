# Generated by Django 3.2.3 on 2021-05-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0009_auto_20210524_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='precio',
            field=models.CharField(max_length=50, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='note',
            name='puntaje1',
            field=models.CharField(max_length=50, verbose_name='Puntaje1'),
        ),
        migrations.AlterField(
            model_name='note',
            name='puntaje2',
            field=models.CharField(max_length=50, verbose_name='Puntaje2'),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='finish',
            field=models.CharField(max_length=50, verbose_name='Termino'),
        ),
    ]