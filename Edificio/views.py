from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from Edificio.models import Sensor, Departamento, Piso, Edificio, User

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

#def registrarEdificio(request):
    return render(request, 'RegistrarEdificio.html')

def registrarEdificio(request):
    if request.method == 'POST':
        # Si el formulario se envía
        nombre_edificio = request.POST['nombre_edificio']
        numero_edificio = request.POST['numero_edificio']
        ubicacion_edificio = request.POST['ubicacion_edificio']
        numero_pisos = request.POST['numero_pisos']

        # Guardar los datos en la base de datos
        edificio = Edificio(
            nombre=nombre_edificio,
            numero=numero_edificio,
            ubicacion=ubicacion_edificio,
            numero_pisos=numero_pisos
        )
        edificio.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('control') 
    
    return render(request, 'RegistrarEdificio.html')

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
        return redirect('RegistrarEdificio')
    return render(request, 'registrar_pisos.html', {'num_pisos': num_pisos})

#def registrarPiso(request):
    if request.method == 'POST':
        # Si el formulario se envía
        num_pisos = request.POST['num_pisos']

        for i in range(1, int(num_pisos) + 1):
            numero_piso = request.POST[f'numero_piso_{i}']

            # Guardar los datos en la base de datos
            piso = Piso(
                numero_piso=numero_piso
            )
            piso.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('RegistrarEdificio')  # Cambia 'pagina_despues_de_guardar.html' por tu propia página
        
    num_pisos = request.GET.get('num_pisos')
    return render(request, 'registrar_pisos.html', {'num_pisos': num_pisos})

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

#def registrarDepartamento(request):
    if request.method == 'POST':
        # Si el formulario se envía
        num_departamentos = request.POST['num_departamentos']

        for i in range(1, int(num_departamentos) + 1):
            nombre_departamento = request.POST[f'nombre_departamento_{i}']
            numero_sensor = request.POST[f'numero_sensor_{i}']

            # Guardar los datos en la base de datos
            departamento = Departamento(
                nombre_departamento=nombre_departamento,
                numero_sensor=numero_sensor
            )
            departamento.save()

        # Redireccionar a alguna página después de guardar los datos
        return redirect('registrar_pisos')  
        
    return render(request, 'registrar_departamentos.html')


def registrarSensor(request):
    if request.method == 'GET':
        return render(request, 'registrar_sensor.html')
    elif request.method == 'POST':
        # Si el formulario se envía
        nombre_edificio = request.POST['nombre_edificio']
        numero_edificio = request.POST['numero_edificio']
        numero_piso_edificio = request.POST['numero_piso_edificio']
        nombre_departamento = request.POST['nombre_departamento']
        datos_sensor = request.POST['datos_sensor']
        consumo_sensor = request.POST['consumo_sensor']
        
        # Guardar los datos en la base de datos
        sensor = Sensor(
            nombre_edificio=nombre_edificio,
            numero_edificio=numero_edificio,
            numero_piso_edificio=numero_piso_edificio,
            nombre_departamento=nombre_departamento,
            datos_sensor=datos_sensor,
            consumo_sensor=consumo_sensor,
        )
        sensor.save()
        
        # Redireccionar a alguna página después de guardar los datos
        return redirect('registrar_departamentos')  


def accederEdificio(request):
    return render(request, 'AccederEdificio.html')

def control(request):
    return render(request, 'control.html')


