from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    sensor_departamento = models.IntegerField()

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
#    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, default=None)
    numero_piso = models.IntegerField()
    contador_piso = models.IntegerField()

class Sensor(models.Model):
    consumo_anterior = models.FloatField()
    consumo_actual = models.FloatField()
    consumo_sensor = models.FloatField()
#    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default=None)

