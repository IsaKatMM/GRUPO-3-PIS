# Generated by Django 5.0.1 on 2024-02-24 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Edificio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edificio',
            old_name='numero',
            new_name='numero_id',
        ),
    ]