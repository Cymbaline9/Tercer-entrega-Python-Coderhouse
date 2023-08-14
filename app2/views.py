from django.shortcuts import render
from app2.models import Curso, Alumno, Profesor
from django.template import loader
from django.http import HttpResponse
from app2.forms import Curso_form, Alumno_form, Profesor_form
# Create your views here.

def inicio(request):
    return render( request , "index.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantillas = loader.get_template("plantillas.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)


"""
def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)
"""



def profesores(request):
    return render( request , "profesores.html")

def info_profesores(request):
    return render( request , "info_profesores.html")

def alta_profesor(request):
    if request.method == "POST":
        alta_profesor = Profesor_form( request.POST )
        if alta_profesor.is_valid():
            datos = alta_profesor.cleaned_data
            prof = Profesor( nombre=datos['nombre'] , apellido=datos['apellido'], dni=datos['dni'], email=datos['email'])
            prof.save()
          
            return render( request , "alta_profesores.html")
    return render( request , "alta_profesores.html")


def alumnos(request):
    return render( request , "alumnos.html")

def alta_alumno(request):
    if request.method == "POST":
        alta_alumno = Alumno_form( request.POST )
        if alta_alumno.is_valid():
            datos = alta_alumno.cleaned_data
            prof = Alumno( nombre=datos['nombre'] , apellido=datos['apellido'], dni=datos['dni'], email=datos['email'])
            prof.save()
          
            return render( request , "alta_alumno.html")
    return render( request , "alta_alumno.html")

def info_alumno(request):
    return render( request , "info_alumno.html")

def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos['nombre'] , comision=datos['comision'])
            curso.save()
            return render( request , "formulario.html")
    
    
    return render( request , "formulario.html")




def buscar_curso(request):
    return render( request , "buscar_curso.html")

def buscar_profe(request):
    return render( request , "buscar_profe.html")

def buscar_alumno(request):
    return render( request , "buscar_alumno.html")


def resultado_curso(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
def resultado_alumno(request):
    if request.GET['dni']:
        dni = request.GET['dni']
        alumno = Alumno.objects.filter(dni__icontains = dni)
        return render( request, "resultado_alumno.html", {"alumnos": alumno})
    else:
        return HttpResponse("Campo vacio")    

    
def resultado_profesor(request):

    if request.GET['dni']:
        dni = request.GET['dni']
        profesor = Profesor.objects.filter(dni__icontains = dni)
        return render( request, "resultado_profesores.html", {"profesores": profesor})
    else:
        return HttpResponse("Campo vacio")
    

    
def cursos(request):
    return render( request , "cursos.html")


def mostrar_cursos(request):
    cursos = Curso.objects.all()  
    return render( request, "mostrar_cursos.html", {"cursos":cursos})

def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()  
    return render( request, "info_alumno.html", {"alumnos":alumnos})

def mostrar_profesores(request):
    profesores = Profesor.objects.all()  
    return render( request, "info_profesores.html", {"profesor":profesores})