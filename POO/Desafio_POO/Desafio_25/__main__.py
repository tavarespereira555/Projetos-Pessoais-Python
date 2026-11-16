from Classes_25.Classes_desafio25 import *

def main():
    dist= 7
    entrega= Drone(dist, 10)
    print(f'Frete de {type(entrega). __name__} em {dist}km = {entrega.calc_frete()}')


if __name__ == '__main__':
    main()