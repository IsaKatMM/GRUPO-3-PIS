# Generated by Django 5.0.1 on 2024-02-25 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Edificio', '0002_rename_numero_edificio_numero_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edificio',
            old_name='numero_id',
            new_name='codigo',
        ),
    ]
