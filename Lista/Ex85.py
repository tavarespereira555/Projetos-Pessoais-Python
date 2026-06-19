lista= [[], []]
for i in range(1, 7 + 1):
    num= int(input(f'Digite o {i}o. valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('=-' * 35)
print(f'Lista completa: {lista}')
print(f'Numeros Pares: {lista[0]}')
print(f'Numeros Impares: {lista[1]}')
