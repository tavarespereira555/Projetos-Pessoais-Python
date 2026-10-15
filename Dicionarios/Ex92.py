dados= dict()
from datetime import datetime
for i in range(1):
    dados['nome']= str(input('Nome: '))
    ano= int(input('Ano de nascimento: '))
    dados['idade'] = datetime.now().year - ano
    dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
    if dados ['ctps'] != 0:
        dados['contratacao'] = int(input('Ano de contratacao: '))
        dados['aposentadoria']= (dados['contratacao'] - ano) + 35
        dados['salario'] = float(input('Salario: R$'))
        print('=-' * 40)
        print(dados)
    else:
        print('=-' * 40)
        print(dados)
for k, v in dados.items():
    print(f'  - {k} tem valor de {v}')
#contratacao > 2000
#ano nascimento 1980
#parei aqui na correcao dos exercicio, lembrar de voltar aqui mais para frente