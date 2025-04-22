from django.urls import path
from . import views
from .views import SaludoVista, EsParVista # Para que funcione la vista clase

urlpatterns = [
    path('bienvenida/',views.bienvenido),
    path('verificar/<int:numero>/',views.es_par),
    path('saludo/<str:nombre>/',SaludoVista.as_view()), # vista basada en clase
    path('es_par/<int:numero>/', EsParVista.as_view()), # vista basada en clase
]
