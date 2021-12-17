from django.contrib import admin
from .models import Jugador, Equipo, Estadio #importe all

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Estadio)


# Register your models here.
