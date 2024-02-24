# Generated by Django 5.0.1 on 2024-02-24 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=100)),
                ('sensor_departamento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=255)),
                ('numero_pisos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_piso', models.IntegerField()),
                ('contador_piso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_edificio', models.CharField(max_length=100)),
                ('numero_edificio', models.IntegerField()),
                ('numero_piso_edificio', models.IntegerField()),
                ('nombre_departamento', models.CharField(max_length=100)),
                ('datos_sensor', models.CharField(max_length=100)),
                ('consumo_sensor', models.FloatField()),
            ],
        ),
    ]
