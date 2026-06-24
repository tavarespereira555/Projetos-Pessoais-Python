import random
Jogadores = dict()
comeca = str(input())
if not comeca:
    print('Valores sorteados: ')
    for i in range(1, 4 + 1):
        Jogadores[f'jogador{i}'] = random.randint(1, 6)
for k, v in Jogadores.items():
    print(f'\tO {k} tirou {v}')
print('Ranking dos jogadores: ')
lista= list(Jogadores.items())
for k,v in lista:
    if k == 1:
        lista.insert(v, k)
    elif v < lista[1]:
        lista.insert(v, k)
print(lista)
#tentando entender:
# lista[i][0] → nome do jogador
#lista[i][1] → valor sorteado

