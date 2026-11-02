from Tratamento_de_Erros.Modulos_115.Arquivo_115 import *
from Tratamento_de_Erros.Modulos_115.Interface_115 import *

arq= 'cursoemvideo.txt'
if not ArquivoExiste(arq):
    criarArquivo(arq)
while True:
    titulo('Menu Principal')
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    match resposta:
        case 1:
            titulo('Opcao 1')
            for i in range(0,len(nomes),2):
                print(f'{nomes[i]:<30}  {nomes[i + 1]} anos')
        case 2 :
            titulo('Opcao 2')
            titulo('Novo Cadastro')
            n1= str(input('Nome: '))
            nomes.append(n1)
            while True:
                try:
                    idade=int(input('Idade: '))
                except ValueError:
                    print('\033[31mERRO!!! Digite apenas numero inteiro validos\033[m')
                    continue
                else:
                    nomes.append(idade)
                    break

            print(f'Novo registro de {n1} adicionado')
        case 3:
            titulo('Opcao 3')
            titulo('Saindo do sistema... Volte Sempre!!')
            break
        case _:
            print('Opção inválida!')