from Tratamento_de_Erros.Modulos_115.Arquivo_115 import titulo


def ArquivoExiste(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a= open(nome, 'wt+')
        a.close()
    except:
        print('Erro! Não foi possivel criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('Pessoas Cadastradas')
        print(a.read())