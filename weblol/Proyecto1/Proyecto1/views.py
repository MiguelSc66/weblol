from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Hola mundo")

def probando(request):
    
    miHtml = open("C:/Users/Equipo/Desktop/weblol/Proyecto1/Proyecto1/plantillas/template1.html")

    platillas = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documentos = platillas.render(miContexto)
    """
    platilla = loader.get_template("template1.html")
    documento = plantilla.render(dicc)
    """
    return HttpResponse(documentos)