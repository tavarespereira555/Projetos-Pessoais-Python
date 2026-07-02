analise= dict()
lista= []
analise['nome']= str(input('Nome do jogador: '))
partidas= int(input(f'Quantas partidas {analise['nome']} jogou? '))
for i in range(partidas):
    lista.append(int(input(f'Quantos gols na partida {i + 1}?? ')))
    analise['gols']=  lista
analise['total'] = sum(lista)
print('=-' * 35)
print(analise)
print('=-' * 35)
for k, v in analise.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 35)
print(f'O jogador {analise['nome']} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'\t=> Na partida {i + 1}, fez {lista[i]} gols')
print(f'Foi um total de {sum(lista)}')