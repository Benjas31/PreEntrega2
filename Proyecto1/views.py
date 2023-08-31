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
   
    mi_html = open('/PRIMER REPOSITORIO/Proyecto1/Proyecto1/templates/template1.html', 'r')
   
    plantilla = Template(mi_html.read()) # Se carga en memoria nuestro documento
    # OJO: Importar Template y Context con: from django.template import Template, Context
   
    mi_html.close() # Cerramos el archivo
   
    mi_contexto = Context(diccionario) # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(mi_contexto) # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)