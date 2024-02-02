from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'Nosotros.html')


def servicio(request):
    return render(request, 'Servicio.html')


def contacto(request):
    return render(request, 'contacto.html')


def iniciarSesion(request):
    if request.method == 'GET':
        print('Enviando formulario')
    else:
        print(request.POST)
        print('Obteniendo formulario')
    return render(request, 'iniciarSesion.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado sastifactoriamente')

            except IntegrityError:
                error = 'El usuario ya existe'
                print(error)
                return render(request, 'registro.html', {"error":error})

        error = 'Las contrasenas no coinciden'
        print(error)
        return render(request, 'registro.html')


def sistema(request):
    return render(request, 'Sistema.html')
