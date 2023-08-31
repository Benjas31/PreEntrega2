from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader
import datetime

def saludo(request):
    return HttpResponse("Hola mundo")

def diaDeHoy(request):
        dia = datetime.datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)

def probando_template(request):
   
    nom = "Nicolas"
    ap = "Perez"
    lista_de_notas = [1,2,3,5,8,3,2]
    
    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now(), "notas": lista_de_notas} # <---- Para enviar al contexto
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario) # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)