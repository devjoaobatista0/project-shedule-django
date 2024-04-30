
from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('search', views.search, name = 'search' ), 
    path('', views.index, name = 'index' ),

    #contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name = 'contact' ), #NOVA URL RECENDO O PARAMETRO PASSANDO O TIPO INT 'ID'
    path('contact/create/', views.create, name = 'create' ), #NOVA URL RECENDO O PARAMETRO PASSANDO O TIPO INT 'ID'
    path('contact/<int:contact_id>/update', views.update, name = 'update' ), #NOVA URL PARA QUANDO EU CRIAR O CONTATO.
    path('contact/<int:contact_id>/delete', views.delete, name = 'delete' ), #NOVA URL PARA QUANDO EU CRIAR O CONTATO.
     
     
     
    path('user/create/', views.register, name = 'register' ), #NOVA URL RECENDO O PARAMETRO PASSANDO O TIPO INT 'ID'
    
]