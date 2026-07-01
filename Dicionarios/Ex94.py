dados= dict()
lista= []
soma= 0
while True:
    dados['nome']= str(input('Nome: '))
    dados['sexo']= str(input('Sexo: [M/F]'))
    dados['idade']= float(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    dados.clear()
    conti= str(input('Deseja continuar?? [S/N]: '))
    if conti in 'Nn':
        break
print('=-' * 40)
print(lista)
print(f'- O grupo possui {len(lista)} pessoas')
print(f'- A media de idade e de {soma / len(lista)} anos.')
for i, v in enumerate(lista):



