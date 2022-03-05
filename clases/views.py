from django.http import HttpResponse
from django.shortcuts import render
from clases.models import Curso
import random


def nuevo_curso(request):
    camada= random.randrange(1500,3000)
    nuevo_curso=Curso(nombre="CursoJS", apellido="pepe", email="hola@hola.com")
    nuevo_curso.save()
    return HttpResponse(f"se creo el curso{nuevo_curso.nombre}, apellido{nuevo_curso.apellido}, email {nuevo_curso.email}")
