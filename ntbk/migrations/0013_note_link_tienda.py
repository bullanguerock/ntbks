# Generated by Django 3.2.3 on 2021-05-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0012_note_id_rutina'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='link_tienda',
            field=models.CharField(default=1, max_length=150, verbose_name='Link Tienda'),
            preserve_default=False,
        ),
    ]