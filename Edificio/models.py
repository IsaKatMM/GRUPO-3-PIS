from django.db import models

# Create your models here.
class Sensor(models.Model):
    nombre_edificio = models.CharField(max_length=100)
    numero_edificio = models.IntegerField()
    numero_piso_edificio = models.IntegerField()
    nombre_departamento = models.CharField(max_length=100)
    datos_sensor = models.CharField(max_length=100)
    consumo_sensor = models.FloatField()
