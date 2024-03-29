from django.db import models
import uuid

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    ubicacion = models.CharField(max_length=100)
    numero_pisos = models.PositiveIntegerField()  # Cambiado a PositiveIntegerField
    
    def __str__(self):
        return self.nombre

class Piso(models.Model):
    consumo_anterior = models.FloatField()
    consumo_actual = models.FloatField()
    consumo_sensor = models.FloatField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    codigo_edificio = models.CharField(max_length=100) 
    piso_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Se usa UUIDField para el ID del piso
    
    def __str__(self):
        return f"Piso de {self.edificio.nombre}"

    from django.db import models

class GeneracionEolica(models.Model):
    velocidad_viento = models.FloatField()

    def generar_energia(self):
        # Implementa la lógica para calcular la energía generada aquí
        # Por ejemplo, multiplicamos la velocidad del viento por un factor constante
        factor_conversion = 10  # Este es solo un ejemplo, ajusta según sea necesario
        energia_generada = self.velocidad_viento * factor_conversion
        return energia_generada


