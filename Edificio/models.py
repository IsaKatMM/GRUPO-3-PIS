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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    sensor_departamento = models.IntegerField()

    # Opcional: puedes agregar más campos según sea necesario
    
    def __str__(self):
        return self.nombre_departamento

class Piso(models.Model):
    numero_piso = models.IntegerField()
    contador_piso = models.IntegerField()

    # Opcional: puedes agregar más campos según sea necesario
    
    def __str__(self):
        return f"Piso {self.numero_piso}"

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    ubicacion = models.CharField(max_length=255)
    numero_pisos = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Opcional: puedes agregar más campos según sea necesario
    
    def __str__(self):
        return self.nombre
