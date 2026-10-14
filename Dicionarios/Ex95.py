analise= dict()
ListaGols= []
lista= []
while True:
    print('----------------------------------------------')
    analise.clear()
    ListaGols.clear()
    analise['nome']= str(input('Nome do jogador: '))
    partidas= int(input(f'Quantas partidas {analise['nome']} jogou? '))
    for i in range(partidas):
        ListaGols.append(int(input(f'Quantos gols na partida {i + 1}?? ')))
    analise['gols']=  ListaGols[:]
    analise['total'] = sum(ListaGols)
    lista.append(analise.copy())
    while True:
        conti= str(input('Deseja continuar??? [S/N]: ')).upper()
        if conti in 'SN':
            break
        print('ERRO!! Responda S ou N')
    if conti in 'Nn':
        break
print('=-' * 35)
print('cod ', end= '')
for k in analise.keys():
    print(f'{k:<15}', end='')
#print(f'{"Cod":<4}{"Nome":<15}{"Gols":^16}{"Total":>4}')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:<4}{v['nome']:<15}{str(v['gols']):<15}{v['total']:<15}')
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
    print('-' * 30)
    if not achou:
        print(f'ERRO!! Não existe jogador com o codigo {joga}! Tente novamente')
print('<< VOLTE SEMPRE>>')

