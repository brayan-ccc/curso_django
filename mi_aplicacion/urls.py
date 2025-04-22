# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.hola_mundo), # Registrando la ruta para la vista hola mundo
    path('pato/',views.pato),
    path('s/<str:nombre>/',views.saludar), # Registrando una vista con parametros
    path('plantilla/<str:nombre>/',views.usando_plantillas),
    path('productos/',views.lista_productos),
    path('',views.inicio),
]
