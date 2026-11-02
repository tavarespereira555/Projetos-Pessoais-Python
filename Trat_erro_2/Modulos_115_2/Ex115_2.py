from Trat_erro_2.Modulos_115_2.Interface_115 import lerArquivo
from Arquivo_115 import *
from Trat_erro_2.Modulos_115_2.Interface_115 import *

arq= 'cursoemvideo.txt'
if not ArquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        titulo('Opcao 1',2 )
        lerArquivo(arq)
    elif resposta == 2:
        titulo('Opcao 2',2)
        nome= str(input('Nome: '))
        idade= leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema',2)
        break
    else:
        print('Erro! Digite apenas numeros validos')