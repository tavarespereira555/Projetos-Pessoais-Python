from Classes.Poligono import Poligono

class Circulo(Poligono):
    def __init__(self, qnt_lados):
        super().__init__(qnt_lados)

    def perimetro(self):
        c= 3.14 * 2 * self.lados
        return c

    def area(self):
        a= 3.14 * self.lados ** 2
        return a