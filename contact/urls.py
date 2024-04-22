
from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name = 'contact' ), #NOVA URL RECENDO O PARAMETRO PASSANDO O TIPO INT 'ID'
    path('search', views.search, name = 'search' ), 
    path('', views.index, name = 'index' ),
]
