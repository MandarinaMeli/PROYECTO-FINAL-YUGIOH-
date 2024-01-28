from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Serie(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)

class Juego(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)


class Pelicula(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)


#class AvatarImagen(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #imagen = models.ImageField(   upload_to="avatares", null=True, black=True)
 