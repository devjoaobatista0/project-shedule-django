from .contact_views import *
from .contact_forms import *   #IMPORTANDO MINHA VIEW DO CREATE CONTACT
from .user_forms import *

"""O arquivo __init__.py em um diretório Python serve para indicar ao interpretador Python que o diretório deve ser considerado um pacote Python. Isso significa que ele pode conter
módulos e subpacotes. Sem o arquivo __init__.py, o Python não reconhecerá o diretório como um pacote e não permitirá a importação de seus conteúdos.
Além disso, o __init__.py pode ser usado para inicializar o pacote, executando código quando o pacote é importado. Isso pode ser útil para configurar variáveis de ambiente, 
registrarclasses ou funções, ou realizar qualquer outra inicialização necessária para o pacote funcionar corretamente."""