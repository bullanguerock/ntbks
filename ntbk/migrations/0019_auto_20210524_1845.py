# Generated by Django 3.2.3 on 2021-05-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0018_note_precioint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='puntaje1',
            field=models.IntegerField(default=0, verbose_name='Puntaje1'),
        ),
        migrations.AlterField(
            model_name='note',
            name='puntaje2',
            field=models.IntegerField(default=0, verbose_name='Puntaje2'),
        ),
    ]
