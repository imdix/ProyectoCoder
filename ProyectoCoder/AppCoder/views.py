from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estadio


# Create your views here.
from ProyectoCoder.AppCoder.models import Equipo


def inicio(request):
    #return HttpResponse("Prueba de inicio")
    return render(request, 'AppCoder/inicio.html')
def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')
def equipos(request):
    return render(request, 'AppCoder/equipos.html')
def estadios(request):
    return render(request, 'AppCoder/estadios.html')
def estadioFormulario(request):
    if request.method == 'POST':
        estadioInsta = Estadio(nombre=request.POST["nombre"], capacidad=request.POST["capacidad"])
        estadioInsta.save()
        return render(request, 'AppCoder/inicio.html')
    return render(request, 'AppCoder/estadioFormulario.html')
def equipoFormulario(request):
    if request.method == 'POST':
        equipoInsta = ProyectoCoder.AppCoder.models.Equipo(club=request.POST["club"], hinchas=request.POST["hinchas"], esGrande=request.POST["esGrande"])
        equipoInsta.save()
        return render(request, 'AppCoder/inicio.html')
    return render(request, 'AppCoder/equipoFormulario.html')