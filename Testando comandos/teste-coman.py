import random
menor= 999999999999999
lista= []
m= 0
for i in range(10):
    num= random.randint(1,100)
    lista.append(num)
    if menor > num:
        menor= num
m= sum(lista) / len(lista)
print(lista)
print(f'Menor: {menor}')
print(f'Media: {m}')
