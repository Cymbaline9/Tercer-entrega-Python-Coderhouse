from django.urls import path
from . import views 

urlpatterns = [
    path("" , views.inicio , name="home"),
    #path("ver_cursos" , views.ver_cursos),
    #path("alta_curso/<str:nombre>/<int:comision>" , views.alta_curso),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso" , views.buscar_curso,name="buscar_curso"),
    path("resultado_curso", views.resultado_curso, name="resultado_curso"),
    path("cursos" , views.cursos, name="cursos"),
    path("mostrar_cursos", views.mostrar_cursos, name="mostrar_cursos"),
    path("info_profesores", views.info_profesores, name="info_profesores"),
    path("alta_profesor", views.alta_profesor, name="alta_profesor"),
    path("buscar_profe" , views.buscar_profe,name="buscar_profe"),
    path("buscar_alumno" , views.buscar_alumno,name="buscar_alumno"),
    path("alta_alumno", views.alta_alumno, name="alta_alumno"),
    path("resultado_alumno", views.resultado_alumno),
    path("resultado_profesor", views.resultado_profesor),
    path("info_alumno", views.info_alumno, name="info_alumno"),
]

