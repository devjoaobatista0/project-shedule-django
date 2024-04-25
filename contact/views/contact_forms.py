
from django.shortcuts import render
from contact.forms import ContactForm





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