from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from Repetix.models import  Piso, Edificio
from django.contrib import messages
from django.http import JsonResponse

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

def registrarPiso2(request):
    return render(request, 'RegistrarEdificio2.html')

def registrarEdificio(request):
    edificio = Edificio.objects.all()
    
    if request.method == 'POST':
    
        nombre_edificio = request.POST['nombre_edificio']
        codigo_edificio = request.POST['codigo_edificio']
        ubicacion_edificio = request.POST['ubicacion_edificio']
        numero_pisos = request.POST['numero_pisos']
    
        edificio = Edificio.objects.create(
            nombre=nombre_edificio,
            codigo=codigo_edificio,
            ubicacion=ubicacion_edificio,
            numero_pisos=numero_pisos
        )
    
        edificio.save()
    
        messages.success(request, 'Edificios Registrados!')
    
        return redirect('AccederEdificio')
    return render(request, 'RegistrarEdificio2.html', {"edificio": edificio})



def edicion(request, codigo):
    edificio = Edificio.objects.get(codigo=codigo)
    return render(request, "EdicionEdificio.html", {"edificio": edificio})

def editarEdificio(request):
    
    nombre_edificio = request.POST['nombre_edificio']
    codigo = request.POST['numero_edificio']
    ubicacion_edificio = request.POST['ubicacion_edificio']
    numero_pisos = request.POST['numero_pisos']
    
    edificio = Edificio.objects.get(codigo=codigo)
    edificio.nombre = nombre_edificio
    edificio.ubicacion = ubicacion_edificio
    edificio.numero_pisos = numero_pisos
    edificio.save()
    
    messages.success(request, 'Edificios Editados!')
    
    return redirect('AccederEdificio')

def eliminacion2(request, codigo):
    edificio = Edificio.objects.get(codigo=codigo)
    edificio.delete()
    
    messages.success(request, 'Edificio Eliminados!')
    
    return redirect('RegistrarEdificio2')

def eliminacion(request, codigo):
    edificio = Edificio.objects.get(codigo=codigo)
    edificio.delete()
    
    messages.success(request, 'Edificio Eliminados!')
    
    return redirect('AccederEdificio')


def accederEdificio(request):
    # Recupera los datos de cada clase desde la base de datos
    edificio = Edificio.objects.all()
    pisos = Piso.objects.all()


    # Pasa los datos recuperados a la plantilla mediante el contexto de renderización
    return render(request, 'AccederEdificio.html', {
        'edificio': edificio,
        'pisos': pisos,
    })


def control(request):
    return render(request, 'control.html')

def contador(request):
    return render(request, 'contador.html')


def registrar_piso(request):
    if request.method == 'POST':
        consumo_anterior = request.POST.get('consumo_anterior')
        consumo_actual = request.POST.get('consumo_actual')
        consumo_sensor = request.POST.get('consumo_sensor')
        codigo_edificio = request.POST.get('codigo_edificio')
        edificio = get_object_or_404(Edificio, codigo=codigo_edificio)
        
        # Crear un nuevo objeto Piso
        nuevo_piso = Piso(
            consumo_anterior=consumo_anterior,
            consumo_actual=consumo_actual,
            consumo_sensor=consumo_sensor,
            edificio=edificio
        )
        
        # Guardar el nuevo piso en la base de datos
        nuevo_piso.save()
        
        # Envía un mensaje de éxito
        messages.success(request, 'Piso registrado con éxito.')

        # Devolver una respuesta JSON indicando que el piso se registró con éxito
        return JsonResponse({'success': True})
    else:
        # Si la solicitud no es POST, devolver un error
        return JsonResponse({'error': 'Método no permitido'}, status=405)