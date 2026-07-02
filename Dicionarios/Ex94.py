dados= dict()
lista= []
soma= 0
m= 0
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
m= soma / len(lista)
print(f'- A media de idade e de {soma / len(lista)} anos.')
print(f'- As mulheres cadastradas foram: ')
for i, v in enumerate(lista):
    if lista[i]['sexo'] in 'Ff':
        print(lista[i]['nome'])
print(f'- Lista de pessoas acima da media: ')
for i, v in enumerate(lista):
    if lista[i]['idade'] > m:
        print(f'Nome = {lista[i]["nome"]}; sexo = {lista[i]["sexo"]}; idade = {lista[i]["idade"]}; ')
print('<< ENCERRADO >>')

