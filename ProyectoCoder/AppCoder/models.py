from django.db import models
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
