from django.urls import path
from lol.views import *

urlpatterns = [
    path('', home, name='home'),
    path("usuario/", usuario),
    path("random/", Random),
]