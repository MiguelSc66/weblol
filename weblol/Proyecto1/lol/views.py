from django.shortcuts import render
from django.http import HttpResponse
from lol.models import Usario

# Create your views here.

def home(request):
    return render(request, "lol/home.html")

def usuario(request):
    return render(request, 'usuario.html')

def Random():
    return HttpResponse('<h1>Random</h1>')

