from django.core.exceptions import ValidationError  #GERAR ERROS
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm): #CLASSE DO PYTHON PARA CRIAR FORM. CRIANDO UM FORM BASEADO NO NOSSO MODEL JA FEITO.
  
    picture = forms.ImageField(       # REFAZENDO O MODEL 'PICTURE' POIS NO NORMAL DO DJANGO ELE DEIXA O LINK DA IMAGEM ENVIADA EXPOSTO. 
                                      # estou dizendo que o unico widget que quero no campo é o de escolha de arquivo.
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
     
     # PEGA OS CAMPO DIRETO DO MODELS JA COM OS PARAMETROS DE CADA UM, 'description por exemplo '
     # esta no model como uma 'text area'.
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone','email', 'description', 'category', 'picture',)  
       
        
      
      
    # METODO 'CLEAN' GERALMENTE USADO QUANDO ESTOU VALIDANDO UM CAMPO QUE DEPENDE DE OUTRO CAMPO, UMA COISA QUE NAO ESTA RELACIONADA COM O CAMPO EM SI.
    def clean(self): #CHAMADO ANTES DE SALVAR OS DADOS NO DB PARA MOSTRAR O ERRO PRO USUARIO
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('Primeiro nome não pode ser igual ao segundo', code='invalid')
            
            self.add_error('first_name',msg)#QUAL CAMPO EU QUERO ADICIONAR A MENSAGEM DE ERRO.
            self.add_error('last_name', msg)
        
        return super().clean()
    
    
    #METODO PARA VALIDAR O CAMPO SOZINHO.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError('Veio do clean_campo', code='invalid')
            )
            
        return first_name  #SE NAO HOUVER ERRO SO VAI RETORNAR O FIRST_NAME.
    
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    
    email = forms.EmailField(
        
    )
    
    class Meta:
        model = User
        fields = (
            
            'first_name', 'last_name','email',
            'username', 'password1', 'password2',   
        )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
            
        if User.objects.filter(email = email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )
            
        return email