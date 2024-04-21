from django.shortcuts import render, get_list_or_404
from contact.models import Contact
from django.http import Http404
# Create your views here.
def index(request):
    contacts = Contact.objects\
            .filter(show=True)\
            .order_by('-id')[:10] #Ordenando por ordem descrecente e configurando o model 'show' como true para quando criar o contato, começar sempre
                                                                 #mostrando, mas se eu quiser desmarcar o 'show' o contato nao aparecer na table.
                                                                 
    print(contacts.query) #VENDO TODAS AS QUERYS QUE O SERVIDOR FEZ.
    
    
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context
    )
    
    
def contact(request, contact_id): #PASSANDO  O contact_id na url atraves do get
    
    single_contact = Contact.objects.filter(id=contact_id, show =True ).first() #RETORNA O UM UNICO VALOR
    
    #single_contact = get_list_or_404(       #POR ALGUM MOTIVO ESSA FUNC NAO ESTAVA RETORNANDO OS DADOS.
        #Contact,pk=contact_id, show = True)
    
    
    if single_contact is None:
        raise Http404()
    
    context = {
        'contact' : single_contact,
    }
    
    return render(
        request,
        'contact/contact.html',
        context,
        
    )