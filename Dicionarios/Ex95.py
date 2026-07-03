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
for k, v in enumerate(lista):
    print(f'{k:<4}{v['nome']:<10}{str(v['gols']):>8}{v['total']:>4}')
print('-' * 40)
while True:
    joga= int(input('Mostrar dados de qual jogador??? (999 para): '))
    if joga == 999:
        break
    achou= False
    for k, v in enumerate(lista):
        if joga == k:
            achou= True
            print(f'-- LEVANTAMENTO DO JOGADOR {v['nome']}:')
            for i, gol in enumerate(v['gols']):
                print(f'No jogo {i + 1} fez {gol} gols')
    if not achou:
        print(f'ERRO!! Não existe jogador com o codigo {joga}! Tente novamente')
print('<< VOLTE SEMPRE>>')

