from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    #return HttpResponse("Prueba de inicio")
    return render(request, 'AppCoder/inicio.html')
def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')
def equipos(request):
    return render(request, 'AppCoder/equipos.html')
def estadios(request):
    return render(request, 'AppCoder/estadios.html')