
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from contact.forms import ContactForm
from contact.models import Contact





def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':    #FORMULARIO POSTADO. FORM QUE TA RECEBENDO O POST.
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        
        
        if form.is_valid(): #METODO DO FORM DO DJANGO, SALVANDO O FORMULARIO SE ELE FOR VALIDO.
            contact = form.save()
            return redirect('contact:update',
                            contact_id=contact.id ) #PARAMETRO DINAMICO
            
        return render(
            request,
            'contact/create.html',
            context  #DADOS
        )
        
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
            request,
            'contact/create.html',
            context  #DADOS
        )
    
    
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show = True) #PASSANDO O MODEL E O PARAMETRO ID. SE O 'ID' NAO EXISTIR ELE RETORNA O 404.
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':    #FORMULARIO POSTADO. FORM QUE TA RECEBENDO O POST.
        
        form = ContactForm(request.POST,request.FILES ,instance=contact)  #instance=contact é usado para associar o formulário a uma instância específica de um modelo. a variavel esta sendo criada 
                                                            #ja com o id.
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        
        
        if form.is_valid(): #METODO DO FORM DO DJANGO, SALVANDO O FORMULARIO SE ELE FOR VALIDO.
            contact = form.save()
            return redirect('contact:update',
                            contact_id=contact.pk ) #PARAMETRO DINAMICO
            
        return render(
            request,
            'contact/create.html',
            context  #DADOS
        )
        
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
            request,
            'contact/create.html',
            context  #DADOS
        )
    
    
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show = True) #PASSANDO O MODEL E O PARAMETRO ID. SE O 'ID' NAO EXISTIR ELE RETORNA O 404.
    
    
    confirmation = request.POST.get('confirmation', 'no') 
    # Este é um método de dicionário em Python, que é usado para acessar o valor associado a uma chave em um dicionário.
    #o valor padrão 'no' é passado diretamente para o método request.POST.get('confirmation', 'no'). Isso significa que, se a chave 'confirmation' não estiver presente nos dados
    #POST da solicitação HTTP, o valor padrão 'no' será retornado.
    
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    context = {
        'contact' : contact,
        'confirmation': confirmation,
    }
    return render(
        request,
        'contact/contact.html',
        context,
    )
    