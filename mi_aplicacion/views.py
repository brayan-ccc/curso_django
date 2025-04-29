from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # Importanto http response para renderizar respuestas sin HTML
from datetime import datetime
from .models import Curso
from .forms import ContactoForm


# Create your views here.

def hola_mundo(request):
    return HttpResponse("<h1>Hola mundo, mi nombre es Brayan</h1>")

def pato(request):
    return HttpResponse("Cuack 🦆")

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}")

# Vista que usa la plantilla hola.html
def usando_plantillas(request, nombre):
    datos_persona = {
        'nombre': nombre,
        'edad':9,
        'fecha': datetime.now()
    }
    return render(request,'mi_aplicacion/hola.html',datos_persona) 
    # return render(request,DÓNDE,QUÉ)

def lista_productos(request):
    productos = [
        {'nombre':'Monitor','precio':1250},
        {'nombre':'Mouse','precio':120},
        {'nombre':'Teclado','precio':200},
        {'nombre':'Laptop','precio':3200},
        {'nombre':'Disco duro','precio':285},
    ]
    return render(request,'mi_aplicacion/productos.html',{"productos":productos})

def inicio(request):
    datos_sitio = { 
        'Mensaje':'Hola',
        'fecha': datetime.now()
    }
    return render(request,'mi_aplicacion/index.html',datos_sitio)

def contactos(request):
    return render(request,'mi_aplicacion/contactos.html')

def estudiantes(request):
    return render(request,'mi_aplicacion/estudiantes.html')

def detalle_curso(request,curso_id):
    # Obtenemos el curso por su ID, SI no existe devolverá un ERROR 404
    curso = get_object_or_404(Curso, id=curso_id)

    # PRIMERA CONSULTA ORM
    estudiantes = curso.estudiantes.all()

    return render(request,'mi_aplicacion/detalle_curso.html',{'curso':curso,'estudiantes':estudiantes})

def contactos(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
           
            # Aquí agregaremos la lógica para guardar los datos en la BASE DE DATOS

            return render(request,'mi_aplicacion/gracias.html')


    else:
        form = ContactoForm()
    
    return render(request,'mi_aplicacion/contactos.html',{'form':form})

