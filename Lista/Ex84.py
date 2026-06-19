lista= []
listanum= []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    pe= float(input('Peso: '))
    lista.append(pe)
    if len(listanum) == 0:
        maior = menor = 0
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    listanum.append(lista[:])
    lista.clear()
    conti= str(input('Deseja continuar?? [S/N]')).upper().strip()
    if conti == 'N':
        break
print('=-' * 35)
print(f'Mais pesado: {maior}Kg. Peso de ' , end= '')
for i in listanum:
    if listanum[1] == maior:
        print(f'{listanum[0]}' , end= '')
print()
print(f'Mais leve: {menor}Kg. Peso de', end='')
for i in listanum:
    if listanum[1] == menor:
        print(f'{listanum[0]}', end='')
print()
print(f'Quantidade de pessoas {len(listanum)}')
"""
lista= []
listanum= []
while True:
    lista.append(str(input('Nome: ')))
    pe= float(input('Peso: '))
    lista.append(pe)
    listanum.append(lista[:])
    lista.clear()
    conti= str(input('Deseja continuar?? [S/N]')).upper().strip()
    if conti == 'N':
        break
maior = menor = listanum[0][1]
nome_leve = []
nome_pesado = []
for i in listanum:
    if i[1] > maior:
        maior= i[1]
        nome_pesado = [i[0]]
    elif i[1] == maior:
        nome_pesado.append(i[0])
    if i[1] < menor:
        menor= i[1]
        nome_leve = [i[0]]
    elif i[1] == menor:
        nome_leve.append(i[0])
print('=-' * 35)
print(f'Mais pesado: {maior}Kg. Peso de {nome_pesado}')
print(f'Mais leve: {menor}Kg. Peso de {nome_leve}')
print(f'Quantidade de pessoas {len(listanum)}') 

Minha resolucao
"""
