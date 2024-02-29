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
    path('Informe/', views.informe, name='Informe'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('recuperarContrasena/', views.recuperacion, name='recuperarContrasena'), 
    path('registrar_piso/', views.registrar_piso, name='registrar_piso'),
    path('RegistrarEdificio2/', views.registrarEdificio, name='RegistrarEdificio2'),
    path('AccederEdificio/', views.accederEdificio, name='AccederEdificio'),
    path('control/', views.control, name='control'),
    path('EdicionEdificio/<codigo>', views.edicion, name='EdicionEdificio'),
    path('EditarEdificio/', views.editarEdificio, name='EditarEdificio'),
    path('EliminarEdificio/<codigo>', views.eliminacion, name='EliminarEdificio'),
]
