from django.core.exceptions import ValidationError  #GERAR ERROS
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm): #CLASSE DO PYTHON PARA CRIAR FORM. CRIANDO UM FORM BASEADO NO NOSSO MODEL JA FEITO.
  
    picture = forms.ImageField(       # REFAZENDO O MODEL 'PICTURE' POIS NO NORMAL DO DJANGO ELE DEIXA O LINK DA IMAGEM ENVIADA EXPOSTO. 
        required=False,                            # estou dizendo que o unico widget que quero no campo é o de escolha de arquivo.
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
        
        if first_name.lower() == 'abc':
            self.add_error(
                'first_name',
                ValidationError('Ta brincando de alfabeto ?', code='invalid')
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
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
    
    def save(self, commit= True):    #SOBREESCREVENDO ESSE METODO PARA PEGAR OS DADOS DO MEU USUARIO SEM SALVAR.
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get('password1') 
        
        if password:
            user.set_password(password) #SETANDO O PASSWORD DE FORMA CRIPTOGRAFADA. PARA A MUDANÇA DE PASSWORD.
            
        if commit:
            user.save()
        
        
    def clean(self):  # SOBREESCREVENDO O CLEAN E CHECANDO SE O PASS 1 É IGUAL AO PASS 2.
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas devem coincidir')
                )
        return super().clean() 
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email #PEGANDO EMAIL ATUAL
        
        if current_email != email: 
            if User.objects.filter(email = email).exists():
                self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )
            
        return email
    
    def clean_password1(self):  #CHECANDO SE O PASS TEM ERROS
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
            
        return password1