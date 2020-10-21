"""Posts Views"""

#Django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

#Utilidades
from datetime import datetime

@login_required
def list_posts(request):

    posts = [
        {
            'titulo': 'Curso de Prospección Online',
            'autor': 'Eric Worre',
            'descripcion': 'Este será un curso genial',
            'foto': 'https://source.unsplash.com/umchkHwkdyM'
        },
        {
            'titulo': 'Curso de Comunicación Efectiva',
            'autor': 'Oscar Torres',
            'descripcion': 'Este será un curso genial',
            'foto': 'https://source.unsplash.com/umchkHwkdyP'
        },
        {
            'titulo': 'Curso de Finanzas Personales',
            'autor': 'Bruno Lizarraga',
            'descripcion': 'Este será un curso genial',
            'foto': 'https://source.unsplash.com/umchkHqkdyM'
        },        
    ]
    return render(request,'posts/feed.html', {'posts':posts})