lista= []
#lista= [2,3,5,7,9]
for i in range(5): # for(0,5) ou for(1, 5 + 1)
    num= int(input('Digite o numero: '))
    if len(lista) == 0:
        lista.append(num)
        print('Adicionando ao final da lista...')
    elif num < lista[0]:
        lista.insert(0, num)
        print('Adicionando na posicao 0 da lista...')
    elif num < lista[1]:
        lista.insert(1, num)
        print('Adicionando na posicao 1 da lista...')
    elif num > lista[-1]:
        lista.append(num)
        print('Adicionando ao final da lista...')
print('=-' * 35)
print(f'Os valores digitados em ordem foram {lista}')
"""-----------------------------------------------------------
resolucao guanabara
for i in range(5): # for(0,5) ou for(1, 5 + 1)
    num= int(input('Digite o numero: '))
    if num == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos= 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
                pos += 1"""
