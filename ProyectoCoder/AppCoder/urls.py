from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('estadios', views.estadios, name="Estadios"),
    path('estadioFormulario', views.estadioFormulario, name="EstadioFormulario"),
    path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"),
]
