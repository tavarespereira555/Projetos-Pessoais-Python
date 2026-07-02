analise= dict()
ListaGols= []
lista= []
while True:
    print('----------------------------------------------')
    analise['nome']= str(input('Nome do jogador: '))
    partidas= int(input(f'Quantas partidas {analise['nome']} jogou? '))
    for i in range(partidas):
        ListaGols.append(int(input(f'Quantos gols na partida {i + 1}?? ')))
    analise['gols']=  ListaGols[:]
    analise['total'] = sum(ListaGols)
    ListaGols.clear()
    lista.append(analise.copy())
    analise.clear()
    conti= str(input('Deseja continuar??? [S/N]: '))
    if conti in 'Nn':
        break
print('=-' * 35)
print(f'{"Cod":<4}{"Nome":<10}{"Gols".center(20)}{"Total":>4}')
print('-' * 40)
for posi,(k, v) in enumerate(lista, start=0):
    print(f'{posi} {lista[0]['nome']}')