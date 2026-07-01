dados= dict()
for i in range(1):
    dados['nome']= str(input('Nome: '))
    ano= int(input('Ano de nascimento: '))
    dados['idade'] = 2026 - ano
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
    print(f'{k} tem valor de {v}')