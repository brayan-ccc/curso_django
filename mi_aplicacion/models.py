from django.db import models

# Create your models here.
# Manejar Clases de Python
class Curso(models.Model): # Uno
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model): # Muchos
    # Por defencto tendremos un campo id auto incrementable de 1 en 1
    # ci = models.CharField(max_length=15,primary_key=True) # Para tener un primary key personalizado
    nombre = models.CharField(max_length=100) # esto hace que el texto tenga como maximo 100 caracteres
    correo = models.EmailField(unique=True) # esto hace que solo pueda haber un correo registrado por estudiante
    fecha_registro = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
