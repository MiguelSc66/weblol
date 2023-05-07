from django.db import models

# Create your models here.

class Usario(models.Model):
    ## apodo
    Nickname = models.CharField(max_length=20)
    ## email
    Email = models.EmailField(max_length=50)
    ## contraseña
    Password = models.CharField(max_length=20)
    ## usar python manage.py check nombre_de_la_app para comprobar el estado 
