from django.contrib import admin
from .models import * #importe all

admin.site.register(Curso)
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Estadio)


# Register your models here.
