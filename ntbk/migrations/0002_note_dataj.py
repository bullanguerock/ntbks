# Generated by Django 3.2.3 on 2021-05-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='dataj',
            field=models.JSONField(default={'accept_list': [], 'reject_list': []}),
        ),
    ]
