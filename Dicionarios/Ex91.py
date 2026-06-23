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
for k,v in Jogadores.items():
    if k == 1:
        #v= #colocar o valor nessa posicao


