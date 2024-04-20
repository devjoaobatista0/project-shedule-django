import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent  #PEGANDO A RAIZ, pois estou importando coisa da raiz do python com o settings, estou dizendo aqui que esse path tambem esta na raiz
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))   #adicionando um caminho acima do arquivo
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'  #passando aonde esta a settings do projeto.
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact #usando os models

    Contact.objects.all().delete() #deletando todos os contatos.
    Category.objects.all().delete() #deletando todas as categories

    fake = faker.Faker('pt_BR')   #todos os dados vao vim em portugues
    categories = ['Amigos', 'Família', 'Conhecidos'] #criando as categories

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()  #salvando na db

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()  #GERA UM DICIONARIO COM PERFIL FAKE
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)  #ESCOLHENDO UMA CATEGORIA ALEATORIA O 'choice' é um modulo do 'RANDOM'

        django_contacts.append(  #JOGANDO OS CONTATOS NA LISTA
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)  #CRIA TODOS OS CONTATOS DE UMA VEZ GERANDO UMA QUERY NA DB
        
        

#EXECUTE O SCRIPT.