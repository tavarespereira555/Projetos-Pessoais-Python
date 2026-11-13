from Classes.Poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, lado= 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        p= self.lado * 4
        return p

    def area(self):
        a= self.lado * self.lado
        return a