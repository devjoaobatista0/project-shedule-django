from django.shortcuts import render, redirect
from contact.forms import RegisterForm 
from django.contrib import messages

def register(request):     #VIEW PADRAO USANDO A CLASSE JA DO DJANGO PARA  CREATE USERS.
    
    form = RegisterForm()
    
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado')  #USANDO FLASH MESSAGES.
            return redirect('contact:index')  #AQUI É A VIEW QUE EU CAPTURAR A MENSAGEM E DEPOIS ELA SERA APAGADA DA MINHA SESSAO
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
    