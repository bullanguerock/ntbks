# Generated by Django 3.2.3 on 2021-05-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntbk', '0003_rename_typr_rutina_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='precio',
            field=models.CharField(default=0, max_length=50, verbose_name='Puntaje CPU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='precioint',
            field=models.IntegerField(default=0, verbose_name='Puntaje CPU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='puntaje1',
            field=models.CharField(default=0, max_length=50, verbose_name='Puntaje CPU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='puntaje2',
            field=models.CharField(default=0, max_length=50, verbose_name='Puntaje CPU'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='almace',
            field=models.CharField(max_length=100, verbose_name='Almacenamiento'),
        ),
        migrations.AlterField(
            model_name='note',
            name='aplicaciones',
            field=models.CharField(max_length=100, verbose_name='Aplicaciones'),
        ),
        migrations.AlterField(
            model_name='note',
            name='bateria',
            field=models.CharField(max_length=100, verbose_name='Bateria'),
        ),
        migrations.AlterField(
            model_name='note',
            name='dimenciones',
            field=models.CharField(max_length=100, verbose_name='Dimen'),
        ),
        migrations.AlterField(
            model_name='note',
            name='gamming',
            field=models.CharField(max_length=100, verbose_name='Gaming'),
        ),
        migrations.AlterField(
            model_name='note',
            name='gpu',
            field=models.CharField(max_length=100, verbose_name='GPU'),
        ),
        migrations.AlterField(
            model_name='note',
            name='gpudedi',
            field=models.CharField(max_length=100, verbose_name='GPU Ded'),
        ),
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.CharField(max_length=100, verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='note',
            name='movilidad',
            field=models.CharField(max_length=100, verbose_name='Movilidad'),
        ),
        migrations.AlterField(
            model_name='note',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pantalla',
            field=models.CharField(max_length=100, verbose_name='Pantalla'),
        ),
        migrations.AlterField(
            model_name='note',
            name='peso',
            field=models.CharField(max_length=100, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='note',
            name='proce',
            field=models.CharField(max_length=100, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='note',
            name='proce_freq',
            field=models.CharField(max_length=100, verbose_name='CPU Freq'),
        ),
        migrations.AlterField(
            model_name='note',
            name='proce_freq_turbo',
            field=models.CharField(max_length=100, verbose_name='CPU Turbo'),
        ),
        migrations.AlterField(
            model_name='note',
            name='proce_hilos',
            field=models.CharField(max_length=100, verbose_name='CPU Hilos'),
        ),
        migrations.AlterField(
            model_name='note',
            name='proce_nucleos',
            field=models.CharField(max_length=100, verbose_name='CPU Nucleos'),
        ),
        migrations.AlterField(
            model_name='note',
            name='puertos',
            field=models.CharField(max_length=100, verbose_name='Puertos'),
        ),
        migrations.AlterField(
            model_name='note',
            name='ram',
            field=models.CharField(max_length=100, verbose_name='RAM'),
        ),
        migrations.AlterField(
            model_name='note',
            name='score_cpu',
            field=models.CharField(max_length=50, verbose_name='Puntaje CPU'),
        ),
        migrations.AlterField(
            model_name='note',
            name='score_gpu',
            field=models.CharField(max_length=50, verbose_name='Puntaje GPU'),
        ),
        migrations.AlterField(
            model_name='note',
            name='so',
            field=models.CharField(max_length=100, verbose_name='S.O.'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tasa_ref',
            field=models.CharField(max_length=100, verbose_name='Tasa Ref'),
        ),
    ]