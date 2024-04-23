from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import Http404
from contact.models import Contact




# Create your views here.
def index(request):
    contacts = Contact.objects\
            .filter(show=True)\
            .order_by('-id') #Ordenando por ordem descrecente e configurando o model 'show' como true para quando criar o contato, começar sempre
                                                                 #mostrando, mas se eu quiser desmarcar o 'show' o contato nao aparecer na table.
    
    paginator = Paginator(contacts, 10, allow_empty_first_page=False)  #FUNCAO PAGINATOR DO DJANGO 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)  
   
                                                     
    # print (contacts.query) #VENDO TODAS AS QUERYS QUE O SERVIDOR FEZ.
    
    
    context = {
        'page_obj': page_obj,    #PASSANDO O PAGE OBJ PRO CONTEXT, POIS AGORA É O PAGE OBJ QUE PEGA OS CONTACTS  
        'site_tittle': 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context  #DADOS
    )
    
def search(request):
    search_value = request.GET.get('q', '').strip() #query dict 'q' = name do form.
    if search_value == '':
        return redirect('contact:index') #FAZENDO O REDIRECT PARA HOME CASO O USUARIO ENVIE O FORM VAZIO PARA EVITAR REQUEST INDESEJADA 
    
    contacts = Contact.objects\
            .filter(show=True)\
            .filter( Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value) )\
            .order_by('-id') #Ordenando por ordem descrecente e configurando o model 'show' como true para quando criar o contato, começar sempre
                                  #mostrando, mas se eu quiser desmarcar o 'show' o contato nao aparecer na table.
    #FILTER 'icontais' = ele passa um (case-sensitive) usado em buscas para nao diferenciar letra maiuscula de minuscla e tenta procurar o que o usuario digitar pelo contexto                                                             
    #print(contacts.query) #VENDO TODAS AS QUERYS QUE O SERVIDOR FEZ.
    paginator = Paginator(contacts, 10, allow_empty_first_page=False)  #FUNCAO PAGINATOR DO DJANGO 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)  
    
    context = {
        'page_obj': page_obj,
        'site_tittle': 'Contatos - '
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
    
    site_tittle = f'{single_contact.first_name} {single_contact.last_name} - ' #COLOCANDO O FIRST E O LAST NAME DO SINGLE CONTATO NO TITTLE DA URL
    
    context = {
        'contact' : single_contact,
        'site_tittle': site_tittle ,
    }
    
    return render(
        request,
        'contact/contact.html',
        context,
        
    )
    
