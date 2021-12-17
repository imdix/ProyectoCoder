from django.db import models
class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField(null=True)

class Equipo(models.Model):
    club = models.CharField(max_length=40)
    hinchas = models.IntegerField()
    esGrande = models.BooleanField(null=True)

class Estadio(models.Model):
    nombre= models.CharField(max_length=40)
    capacidad= models.IntegerField(null=True)

