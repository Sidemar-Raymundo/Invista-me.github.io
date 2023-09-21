from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

#def novo_usuario(request):
   # return(HttpResponse('aqui está o novo usuario'))
def novo_usuario(request):
    # para tratar os dados vindos do usuario como POST no servidor segue o passo a passo abaixo⬇️⬇️
    #tipo, validar, informar
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
         # salvar no banco de dados
            formulario.save()

   # informar
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
        
    else:
         formulario =UserRegisterForm()
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})

   


    
            
        

    