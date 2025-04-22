from django.shortcuts import render
from django.http import HttpResponse # Importanto http response para renderizar respuestas sin HTML
from datetime import datetime
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
