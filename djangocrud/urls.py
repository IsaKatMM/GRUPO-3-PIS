"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from tasks.views import index, iniciarSesion, nosotros, servicio, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('index/', views.index, name='Index'),
    path('Nosotros/', views.nosotros, name='Nosotros'),
    path('Servicio/', views.servicio, name='Servicio'),
    path('contacto/', views.contacto, name='Contacto'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),   
    path('registro/', views.registro, name='Registro'),
    path('tasks/Templates/Sistema.html', views.sistema, name='Sistema'),
    path('tasks/Templates/Sensor.html', views.sensor, name='Sensor'),
    path('tasks/Templates/Actuador.html', views.actuador, name='Actuador'),
    path('tasks/Templates/Edificio.html', views.edificio, name='Edificio'),
    path('tasks/Templates/Piso.html', views.piso, name='Piso'),
    path('tasks/Templates/Informe.html', views.informe, name='Informe'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('recuperarContrasena/', views.recuperacion, name='recuperarContrasena'),
    #path('Signup/', views.signup, name='Signup'),
    #path('tasks/', views.tasks, name='tasks'),
    #path('logout/', views.signout, name='logout'),
    #path('iniciarSesion/', views.iniciarSesion, name='Iniciar Sesion')
]
