from Classes.Classes_desafio29 import *
def main():
    d= Diario('Pular')
    d.escrever('Lindo dia')
    d.escrever('Belos cabelos')
    d.escrever('Opaa')
    d.ler()
    inspect(d, private= True, methods= True)

if __name__ == '__main__':
    main()
