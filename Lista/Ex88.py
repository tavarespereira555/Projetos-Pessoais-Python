import time
import random
lista= []
listaAuxi= list()
print('-' * 40)
print('JOGOS DA MEGA SENA'.center(40))
print('-' * 40)
jogos= int(input('Quantos jogos vc quer q eu sorteie??? '))
print(f'=-=-=-=- SORTEANDO {jogos} JOGOS =-=-=-=-')
for i in range(1, jogos + 1):
    num= random.sample(range(0,61), 6)
    lista.append(num)
    lista.sort()
    listaAuxi.append(lista[:])
    lista.clear()
    print(f'Jogo {i}: {listaAuxi[i -1][0]}')
    time.sleep(1)
print('=-=-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-=-=')