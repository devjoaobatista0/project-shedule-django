from django.contrib import admin
from contact import models
# Register your models here.



@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id', #ID DECRESCENTE
    #list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',  #PROCURAR
    list_per_page = 10 #QUANTOS CONTACTS EXIBIR POR PAG
    list_max_show_all = 200 #QUANTOS CONTATOS ATE APARECER O BOTAO DE 'MOSTRAR TUDO'
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone', 
    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', #ID DECRESCENTE
 