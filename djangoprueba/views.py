"""
Vistas
"""
#Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilidades
from datetime import datetime

def hello_world(request):
    return HttpResponse('Hello, world! The time is {now}'.format(
        now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    ))

def ordenar_enteros(request):

    numbers = request.GET['numbers'].split(",")
    numbers = map(lambda x: int(x), numbers)
    data = {
        "status" : 'ok',
        "numbers" : sorted(numbers)
    }

    return JsonResponse(data, json_dumps_params={'indent': 4})

def hi(request, name, age):

    if age>12:
        msg = 'Bienvenido'
    else:
        msg = 'No puedes ingresar'

    data = {
        "status" : 'ok',
        "nombre" : name,
        "edad"   : age,
        "msg"    : msg,    
    }

    return JsonResponse(data, json_dumps_params={'indent': 4})