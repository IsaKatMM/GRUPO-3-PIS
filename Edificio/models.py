from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sensor(models.Model):
    nombre_edificio = models.CharField(max_length=100)
    numero_edificio = models.IntegerField()
    numero_piso_edificio = models.IntegerField()
    nombre_departamento = models.CharField(max_length=100)
    datos_sensor = models.CharField(max_length=100)
    consumo_sensor = models.FloatField()

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    sensor_departamento = models.IntegerField()

    # Opcional: puedes agregar más campos según sea necesario
    
    def __str__(self):
        return self.nombre_departamento

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    ubicacion = models.CharField(max_length=255)
    numero_pisos = models.IntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)

    
class Piso(models.Model):
    numero_piso = models.IntegerField()
    contador_piso = models.IntegerField()



