from django.urls import path
from Repetix import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('index/', views.index, name='Index'),
    path('Nosotros/', views.nosotros, name='Nosotros'),
    path('Servicio/', views.servicio, name='Servicio'),
    path('contacto/', views.contacto, name='Contacto'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),   
    path('registro/', views.registro, name='Registro'),
    path('Sistema/', views.sistema, name='Sistema'),
    path('tasks/Templates/Sensor.html', views.sensor, name='Sensor'),
    path('tasks/Templates/Actuador.html', views.actuador, name='Actuador'),
    path('tasks/Templates/Edificio.html', views.edificio, name='Edificio'),
    path('tasks/Templates/Piso.html', views.piso, name='Piso'),
    path('Informe/', views.informe, name='Informe'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('recuperarContrasena/', views.recuperacion, name='recuperarContrasena'), 
    path('registrar_piso/', views.registrar_piso, name='registrar_piso'),
    path('RegistrarEdificio2/', views.registrarEdificio, name='RegistrarEdificio2'),
    path('RegistrarPiso/', views.registrarPiso2, name='RegistrarPiso'),
    path('AccederEdificio/', views.accederEdificio, name='AccederEdificio'),
    path('control/', views.control, name='control'),
    path('EdicionEdificio/<codigo>', views.edicion, name='EdicionEdificio'),
    path('EditarEdificio/', views.editarEdificio, name='EditarEdificio'),
    path('EliminarEdificio2/<codigo>', views.eliminacion2, name='EliminarEdificio2'),
    path('EliminarEdificio/<codigo>', views.eliminacion, name='EliminarEdificio'),
    path('contador/', views.contador, name='contador')
]
