# Generated by Django 3.2.3 on 2021-05-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0014_remove_note_link_tienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='items',
            field=models.IntegerField(default=0, verbose_name='Items'),
            preserve_default=False,
        ),
    ]