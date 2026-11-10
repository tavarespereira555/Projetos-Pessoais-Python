from Classes.Poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, qnt_lados):
        super().__init__(qnt_lados)

    def perimetro(self):
        p= self.lados * 4
        return p

    def area(self):
        a= self.lados * self.lados
        return a