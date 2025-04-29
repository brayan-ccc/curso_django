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
    path('contactos/',views.contactos,name='contactos'),
    # path('registrar-estudiante/', views.registrar_estudiante, name='registrar_estudiante'),


    path('estudiantes/',views.estudiantes,name='estudiantes'),
    path('curso/<int:curso_id>/',views.detalle_curso,name='detalle_curso')

]
