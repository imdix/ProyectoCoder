from django.db import models
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    esNoche=models.BooleanField(null=True)
    def __str__(self):
        return f"Curso: {self.nombre} CAMADA: {self.camada} NOCHE: {self.esNoche}"
class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
class Equipo(models.Model):
    nombre= models.CharField(max_length=40)
    hinchas = models.IntegerField()
    esGrande = models.BooleanField()
class Estadio(models.Model):
    nombre= models.CharField(max_length=40)
    capacidad= models.IntegerField()
    esGrande = models.BooleanField()