from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):

    if  request.method == 'POST':

        #Recibimos los datos del post
        username = request.POST['username']
        password = request.POST['password']

        #Autenticacion
        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            return redirect('list_post')

        else:
            return  render(request, 'autores/login.html', {'error': 'Intruso'})
    else:
        return render(request, 'autores/login.html')

