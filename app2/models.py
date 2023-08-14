from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

#    def __str__(self):
#       return f"Curso: {self.nombre}, Comision:{self.comision}"
    


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    materia =models.CharField(max_length=40, default="")