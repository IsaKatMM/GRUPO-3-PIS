from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Sistema')

            except IntegrityError:
                return render(request, 'registro.html', {
                    "error": 'El usuario ya existe'
                })

        return render(request, 'registro.html', {
            "error": 'Las contraseñas no coinciden'
        })

def sistema(request):
    return render(request, 'Sistema.html')

def cerrarSesion(request):
    logout(request)
    return redirect('Index')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.htmL', {
                'error': "El usuario o la contrasena son incorrectos"
            })
        else:
            login(request, user)
            return redirect('Sistema')
        
def sensor(request):
    return render(request, 'Sensor.html')

def actuador(request):
    return render(request, 'Actuador.html')

def edificio(request):
    return render(request, 'Edificio.html')

def piso(request):
    return render(request, 'Piso.html')

def informe(request):
    return render(request, 'Informe.html')

def recuperacion(request):
    return render(request, 'recuperarContrasena.html')

def registrarEdificio(request):
    return render(request, 'RegistrarEdificio.html')

def registrarPiso(request):
    num_pisos = request.GET.get('num_pisos')
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'registrar_pisos.html', {'num_pisos': num_pisos})

def registrarDepartamento(request):
    num_departamentos = request.GET.get('num_departamentos')
    # Aquí puedes agregar lógica adicional si es necesarios
    return render(request, 'registrar_departamentos.html', {'num_departamentos': num_departamentos})

def registrarSensor(request):
    return render(request, 'registrar_sensor.html')


