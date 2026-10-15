import random
menor= 99999
maior= -99999
lista= (random.randint(1, 15), random.randint(1, 15),
        random.randint(1, 15), random.randint(1, 15),
        random.randint(1, 15))
print(f'Os numeros sorteados foram: {lista}')
for i in lista:
    if i > maior:
        maior= i
    if i < menor:
        menor= i
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')