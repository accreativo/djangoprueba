"""Posts Models"""
from autores.models import Autor
from django.db import models

class Post(models.Model):

    #ForgeinKey
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    #Atributtes
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)

    #CreatedUpdated
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.titulo