from typing import Any
from django.shortcuts import render
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError #GERAR ERROS


class ContactForm(forms.ModelForm): #CLASSE DO PYTHON PARA CRIAR FORM. CRIANDO UM FORM BASEADO NO NOSSO MODEL JA FEITO.
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', )   
        
    def clean(self): #CHAMADO ANTES DE SALVAR OS DADOS NO DB PARA MOSTRAR O ERRO PRO USUARIO
        cleaned_data = self.cleaned_data
        
        self.add_error(None, ValidationError('Mensagem de erro', code='invalid'))
    
        self.add_error(None, ValidationError('Mensagem de erro 2', code='invalid'))
        return super().clean()

def create(request):
    if request.method == 'POST':    #FORMULARIO POSTADO. FORM QUE TA RECEBENDO O POST.
        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context  #DADOS
        )
        
    context = {          #FORMULARIO FORA DO IF. FORM LIMPO, ESSE FORM É USADO QUANDO O METODO FOR GET.
         'form': ContactForm()
    }
    
    return render(
            request,
            'contact/create.html',
            context  #DADOS
        )