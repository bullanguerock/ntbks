# Generated by Django 3.2.3 on 2021-05-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0010_auto_20210524_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='solotodo_id',
            field=models.CharField(default=0, max_length=50, verbose_name='ID Solotodo'),
            preserve_default=False,
        ),
    ]