from django.contrib import admin
from .models import Edificio, Piso, Departamento, Sensor

# Register your models here.
admin.site.register(Edificio)

admin.site.register(Piso)

admin.site.register(Departamento)

admin.site.register(Sensor)
