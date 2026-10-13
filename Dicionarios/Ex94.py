dados= dict()
lista= []
soma= 0
m= 0
while True:
    dados['nome']= str(input('Nome: '))
    while True:
        dados['sexo']= str(input('Sexo: [M/F] ')).upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO!! Por favor digite apenas M ou F')
    dados['idade']= float(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    dados.clear()
    while True:
        conti= str(input('Deseja continuar??: [S/N] ')).upper()
        if conti in 'SN':
            break
        print('ERRO!! Por favor digite S ou N')
    if conti in 'Nn':
        break
print('=-' * 40)
print(lista)
print(f'A) O grupo possui {len(lista)} pessoas')
m= soma / len(lista)
print(f'B) A media de idade e de {soma / len(lista):5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ')
for i, v in enumerate(lista):
    if lista[i]['sexo'] in 'Ff':
        print(lista[i]['nome'])
#for p in (galera):
    #if p['nome'] in 'Ff':
        #print(f'{p["nome"]}')
print(f'D) Lista de pessoas acima da media: ')
for i, v in enumerate(lista):
    if lista[i]['idade'] > m:
        print(f'Nome = {lista[i]["nome"]}; sexo = {lista[i]["sexo"]}; idade = {lista[i]["idade"]}; ')
        #print(f'{v}')
print('<< ENCERRADO >>')

