# Generated by Django 3.2.3 on 2021-05-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0013_note_link_tienda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='link_tienda',
        ),
    ]