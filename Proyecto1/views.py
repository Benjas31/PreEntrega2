from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola mundo")

def diaDeHoy(request ):
        dia = datetime.datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)

