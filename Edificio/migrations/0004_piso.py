# Generated by Django 5.0.1 on 2024-02-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edificio', '0003_rename_numero_sensor_departamento_sensor_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_piso', models.IntegerField()),
                ('contador_piso', models.IntegerField()),
            ],
        ),
    ]