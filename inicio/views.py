from django.shortcuts import render

from django.http import HttpResponse
import random

from django.template import Context, Template, loader

def inicio(request):
    return HttpResponse ("Hola, soy la nueva pagina")

def otro_vista(request):
    return HttpResponse(""" 
                        <h1>Este es un titulo en h1</h1>
                        """)
    
def numero_random(request):
    numero= random.randrange(15,180)
    texto=f"""<h1>Este es tu numero random: {numero}</h1>"""
    return HttpResponse(texto)

def numero_del_usuario(request,numero):
    texto=f"""<h1>Este es tu numero: {numero}</h1>"""
    return HttpResponse(texto)

def mi_plantilla(request):
    #   plantilla= open(r"E:\Lauu\PythonCODERHOUSE\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    template=loader.get_template("mi_plantilla.html")
#    template=Template(plantilla.read())
    nombre= "Jorge"
    apellido= "Atahualpa"
    
    lista=[1,2,3,4,5,6,7,8,9]
    
    diccionario_de_datos= {
        "nombre": nombre,
        "apellido": apellido,
        "nombre_largo": len(nombre),
        "lista": lista
    }
 
#    context= Context()
    plantilla_preparada=template.render(diccionario_de_datos)
    return HttpResponse(plantilla_preparada)

