def ficha(n= 'desconhecido', gols= 0):
    if not n:
        n = 'desconhecido'
    if not gols:
        gols= 0
    print(f'O jogador {n} fez {gols} gol(s) no campeonato')



nome= str(input('Nome do jogador: '))
gol= (input('Numero de gols: '))
ficha(nome, gol)