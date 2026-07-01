import random
Jogadores = dict()
come = str(input())
troca= True
if not come:
    print('Valores sorteados: ')
    for i in range(1, 4 + 1):
        Jogadores[f'jogador{i}'] = random.randint(1, 6)
    for k, v in Jogadores.items():
        print(f'\tO {k} tirou {v}')
    print('Ranking dos jogadores: ')
    lista= list(Jogadores.items())
    while troca:
        troca = False
        for i in range(len(lista) -1 ):
            if lista[i][1] <  lista[i + 1][1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                troca = True
    for posi,(P, item) in enumerate(lista, start =1):
        print(f'{posi}°lugar: {P} com {item}')

