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
    path('tasks/Templates/index.html', views.index, name='Index'),
    path('tasks/Templates/Nosotros.html', views.nosotros, name='Nosotros'),
    path('tasks/Templates/Servicio.html', views.servicio, name='Servicio'),
    path('tasks/Templates/contacto.html', views.contacto, name='Contacto'),
    path('tasks/Templates/iniciarSesion.html', views.iniciarSesion, name='iniciarSesion'),   
    #path('', views.nosotros, name='Nosotros'),
    #path('Signup/', views.signup, name='Signup'),
    #path('tasks/', views.tasks, name='tasks'),
    #path('logout/', views.signout, name='logout'),
    #path('iniciarSesion/', views.iniciarSesion, name='Iniciar Sesion')
]
