# Generated by Django 5.0.1 on 2024-02-23 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edificio', '0014_rename_edificio_id_piso_edificio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piso',
            name='edificio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Edificio.edificio'),
        ),
    ]