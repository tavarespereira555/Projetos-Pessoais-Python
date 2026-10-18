import time
import random
numeros = []
num= []
def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    pos = 0
    #for i in range(5):
    while pos < 5:
        nu= random.randint(1,15)
        lista.append(nu)
        print(nu, end=' ')
        time.sleep(0.5)
        pos += 1
    print(' PRONTO!!')
def somaPar(lista):
    somar = 0
    print(f'Somando os valores pares de {lista} ', end=' ')
    for i in lista:
        if i % 2 == 0:
            somar += i
    print(f'Temos {somar}')


sorteia(numeros)
somaPar(numeros)
sorteia(num)

"""
Colocar sem a variavel n= random.randint(1, 15) mostra todos os numeros de uma vez,
caso queira um numero por vez tem q usar a variavel 
 -> n= random.randint(1, 15)
lista.append(n)
print(n)
"""
