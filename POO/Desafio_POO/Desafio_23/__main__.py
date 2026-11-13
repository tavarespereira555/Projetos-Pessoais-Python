from Classes.Poligono import Poligono
from Classes.Quadrado import Quadrado
from Classes.Circulo import Circulo




def main():
    p1= Quadrado(12)
    p2= Circulo(20)
    print(f'Perimetro = {p1.perimetro():.1f}')
    print(f'Lado Quadrado: {p1.lado}')
    print(f'Area = {p1.area():.1f}')
    print('-' * 10)
    print(f'Raio= {p2.raio}')
    print(f'Perimetro = {p2.perimetro():.1f}')
    print(f'Area = {p2.area():.1f}')


if __name__ == '__main__':
    main()