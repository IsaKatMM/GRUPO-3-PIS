from django.urls import path
from Repetix import views
from Repetix.views import GenerarEnergiaEolica

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
    path('control/<codigo>', views.control, name='ControlarEdificio'),
    path('ControlarEdificio/', views.ControlarEdificio, name='ControlarEdificio'),
    path('EliminarEdificio/<codigo>', views.eliminacion, name='EliminarEdificio'),
    path('actualizar_tabla_pisos/', views.actualizar_tabla_pisos, name='actualizar_tabla_pisos'),
    path('energia_eolica/', views.energia_eolica, name='energia_eolica'),
    path('generar_energia_eolica/',views.GenerarEnergiaEolica, name='generar_energia_eolica'),

]

