import dis

from Classes_25.Classes_desafio25 import *
from rich.table import Table
from rich import print

def main():
    dist= 8
    viagem= [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela= Table(title='Tabela de fretes')
    tabela.add_column('Distancia')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')
    for i in viagem:
        tabela.add_row(f'{dist}Km', f'{type(i).__name__}', f'{i.calc_frete()}')
    print(tabela)
if __name__ == '__main__':
    main()