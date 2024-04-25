from django.core.exceptions import ValidationError  #GERAR ERROS
from django import forms
from . import models

class ContactForm(forms.ModelForm): #CLASSE DO PYTHON PARA CRIAR FORM. CRIANDO UM FORM BASEADO NO NOSSO MODEL JA FEITO.
    def __init__( self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )
    
    
     

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', )  
        
        
    def clean(self): #CHAMADO ANTES DE SALVAR OS DADOS NO DB PARA MOSTRAR O ERRO PRO USUARIO
        #cleaned_data = self.cleaned_data
        
        self.add_error(None, ValidationError('Mensagem de erro', code='invalid'))
    
        self.add_error(None, ValidationError('Mensagem de erro 2', code='invalid'))
        return super().clean()