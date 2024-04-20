from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #importando modulo de user para permitir que o 'owner'(proprietario) tenha permissoes
# Create your models here.

#TABELA
class Category(models.Model):
    class Meta:
        verbose_name = 'Category' #Toda vez que eu buscar o singular dessa categoria eu chamo de 'category'
        verbose_name_plural = 'Categories' #Como deve ser chama rno plural
    name = models.CharField(max_length=50)

    
    def __str__(self) -> str:
        return self.name 
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True) #Permite que o campo fica vazio
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank = True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%y/%m/') #CRIANDO A FOLDER PICTURES COM O ANO E MES ATUAL
    category = models.ForeignKey(  #criando model da categoria dependendo de contact
        Category, #Model da categoria 
        on_delete=models.SET_NULL, #quando eu deletar a categoria fazendo que o campo categoria daquele contato fique NULL
        blank=True, null=True  
    )
    owner = models.ForeignKey(
        User, 
        on_delete = models.SET_NULL,
        blank=True,
        null = True,
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'  


