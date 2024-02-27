from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from Repetix.models import Sensor, Departamento, Piso, Edificio
from django.contrib import messages

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

def registrarEdificio2(request):
    
    edificio = Edificio.objects.all()
    
    if request.method == 'POST':
        # Si el formulario se envía
        nombre_edificio = request.POST['nombre_edificio']
        codigo = request.POST['numero_edificio']
        ubicacion_edificio = request.POST['ubicacion_edificio']
        numero_pisos = request.POST['numero_pisos']

        # Guardar los datos en la base de datos
        edificio = Edificio.objects.create(
            nombre=nombre_edificio,
            codigo=codigo,
            ubicacion=ubicacion_edificio,
            numero_pisos=numero_pisos
        )
        edificio.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('RegistrarEdificio2') 
    
    # Si no es un POST, solo renderiza el formulario
    return render(request, 'RegistrarEdificio2.html', {"edificio": edificio})

def registrarEdificio(request):
    
    edificio = Edificio.objects.all()
    
    if request.method == 'POST':
    
        nombre_edificio = request.POST['nombre_edificio']
        codigo = request.POST['numero_edificio']
        ubicacion_edificio = request.POST['ubicacion_edificio']
        numero_pisos = request.POST['numero_pisos']
    
        edificio = Edificio.objects.create(
            nombre=nombre_edificio,
            codigo=codigo,
            ubicacion=ubicacion_edificio,
            numero_pisos=numero_pisos
        )
    
        edificio.save()
    
        messages.success(request, 'Edificios Registrados!')
    
        return redirect('AccederEdificio')
    return render(request, 'RegistrarEdificio.html', {"edificio": edificio})

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

def registrarPiso(request):
    num_pisos = request.GET.get('num_pisos')
    if request.method == 'POST':
        # Si el formulario se envía
        numero_piso = request.POST[f'numero_piso']
        contador_piso = request.POST[f'contador_piso']

        # Guardar los datos en la base de datos
        piso = Piso(
            numero_piso=numero_piso,
            contador_piso=contador_piso
        )
        piso.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('RegistrarEdificio2')
    return render(request, 'registrar_pisos.html', {'num_pisos': num_pisos, })


def registrarDepartamento(request):
    num_departamentos = request.GET.get('num_departamentos')
    if request.method == 'POST':
        # Si el formulario se envía
        nombre_departamento = request.POST[f'nombre_departamento']
        sensor_departamento = request.POST[f'sensor_departamento']

        # Guardar los datos en la base de datos
        departamento = Departamento(
            nombre_departamento=nombre_departamento,
            sensor_departamento=sensor_departamento
        )
        departamento.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('registrar_pisos')
    return render(request, 'registrar_departamentos.html', {'num_departamentos': num_departamentos})

def registrarSensor2(request, id):
    departamento = Departamento.objects.get(sensor_departamento=id)
    return render(request, "registrar_sensor.html", {"departamento": departamento})

def registrarSensor(request, id):
    
    departamento = Departamento.objects.get(sensor_departamento=id)
    
    if request.method == 'POST':
        # Si el formulario se envía
        consumo_anterior = request.POST['consumo_actual']
        consumo_actual = request.POST['consumo_actual']
        consumo_sensor = request.POST['consumo_sensor']
        
        sensor = Sensor(
            consumo_anterior=consumo_anterior,
            consumo_actual=consumo_actual,
            consumo_sensor=consumo_sensor,
        )
        sensor.save()
        
        # Redireccionar a alguna página después de guardar los datos
        return redirect('registrar_departamentos')  
    
    return render(request, 'registrar_sensor.html' , {"departamento": departamento})

def accederEdificio(request):
    # Recupera los datos de cada clase desde la base de datos
    edificio = Edificio.objects.all()
    pisos = Piso.objects.all()
    sensores = Sensor.objects.all()
    departamentos = Departamento.objects.all()

    # Pasa los datos recuperados a la plantilla mediante el contexto de renderización
    return render(request, 'AccederEdificio.html', {
        'edificio': edificio,
        'pisos': pisos,
        'sensores': sensores,
        'departamentos': departamentos,
    })


def control(request):
    return render(request, 'control.html')

def contador(request):
    return render(request, 'contador.html')
