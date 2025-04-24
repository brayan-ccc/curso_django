"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # Importando include
# from mi_aplicacion import views # Importando nuestra vista que está dentro de mi_aplicacion
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hola/', views.hola_mundo), # Registrando la ruta para la vista hola mundo
    # path("pato/",views.pato),
    # path("s/<str:nombre>/",views.saludar), # Registrando una vista con parametros
    path('mi_app/', include('mi_aplicacion.urls')),
    # Aqui registraremos las urls de otras aplicaciones
    path('otra_app/', include('otra_aplicacion.urls')),
    path('',views.inicio,name='ini')
]
