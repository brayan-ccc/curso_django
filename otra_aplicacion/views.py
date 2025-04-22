from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # Importamos View para poder utilizar vistas basadas en clases

# VISTAS BASADAS EN FUNCIONES
def bienvenido(request):
    return HttpResponse("<p>Bienvenido/a a mi otra aplicación</p>")

def es_par(request,numero):
    # De un numero entero, verificar si es PAR o IMPAR
    if numero % 2 == 0:
        return HttpResponse(f"El número {numero} es PAR")
    else:
        return HttpResponse(f"El número {numero} es IMPAR")
    
# VISTAS BASADAS EN CLASES
class SaludoVista(View):
    def get(self, request, nombre):
        return HttpResponse(f"Hola {nombre} desde una CLASE")
    
class EsParVista(View):
    def get(self, request, numero):
        if numero % 2 == 0:
            return HttpResponse(f"El número {numero} es PAR")
        else:
            return HttpResponse(f"El número {numero} es IMPAR")