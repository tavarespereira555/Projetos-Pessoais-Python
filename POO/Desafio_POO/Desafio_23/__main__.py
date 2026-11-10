from Classes.Poligono import Poligono
from Classes.Quadrado import Quadrado
from Classes.Circulo import Circulo




def main():
    p1= Quadrado(12)
    print(f'Perimetro = {p1.perimetro():.1f}')
    print(f'Area = {p1.area():.1f}')


if __name__ == '__main__':
    main()