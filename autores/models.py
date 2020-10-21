"""Autores Models"""

#Django
from django.contrib.auth.models import User
from django.db import models

class Autor(models.Model):
    """ Autor Model """

    #ForgeinKey
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Atributtes
    website = models.URLField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='autores/fotos', blank=True, null=True)

    #CreatedUpdated
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        user = self.user.username
        return user