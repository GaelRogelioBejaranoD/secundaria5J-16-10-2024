from django.shortcuts import render
from .models import AlumnoT, Frase

# Create your views here.

def Index_vista(request):
    misalumnos=AlumnoT.objects.all().order_by("id") # nuevo mas el diccionario
    return render(request, "index.html", {"misalumnos":misalumnos})
