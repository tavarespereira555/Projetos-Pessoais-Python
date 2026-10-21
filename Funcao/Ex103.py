def ficha(n= 'desconhecido', gols= 0):
    print(f'O jogador {n} fez {gols} gol(s) no campeonato')



nome= str(input('Nome do jogador: '))
gol= str(input('Numero de gols: '))
if gol.isnumeric():
    gol= int(gol)
else:
    gol = 0
if not nome:
    ficha(gols= gol)
else:
    ficha(nome, gol)