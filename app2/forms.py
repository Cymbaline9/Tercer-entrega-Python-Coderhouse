from django import forms



class Curso_form(forms.Form):
    nombre =  forms.CharField(max_length=40)
    comision = forms.IntegerField()


class Alumno_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()

class Profesor_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    materia = forms.CharField(max_length=40)