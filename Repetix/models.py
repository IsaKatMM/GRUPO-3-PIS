from django.db import models

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    ubicacion = models.CharField(max_length=100)
    numero_pisos = models.FloatField()
    
    def __str__(self):
        return self.nombre

class Piso(models.Model):
    consumo_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_actual = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_sensor = models.DecimalField(max_digits=10, decimal_places=2)
 #   edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name='pisos')

    def __str__(self):
        return f"Piso de {self.edificio.nombre}"
