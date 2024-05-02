from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):     #VIEW PADRAO USANDO A CLASSE JA DO DJANGO PARA  CREATE USERS.
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado')  #USANDO FLASH MESSAGES.
            return redirect('contact:login')  #AQUI É A VIEW QUE EU CAPTURAR A MENSAGEM E DEPOIS ELA SERA APAGADA DA MINHA SESSAO
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {
                'form' : form
            }
            
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    
    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form' : form
            }
            
        )
        
    form.save()
    return render(
            request,
            'contact/register.html',
            {
                'form' : form
            }
            
        )
    

def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()  # RESPONSAVEL POR SABER SE ESTA TUDO CERTO COM O USUARIO
            auth.login(request, user) #LOGANDO O USUARIO
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')
            
    return render(
        request,
        'contact/login.html',
        {
            'form' : form
        }
    )
    

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')



    