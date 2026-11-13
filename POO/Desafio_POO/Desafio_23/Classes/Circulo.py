from Classes.Poligono import Poligono

class Circulo(Poligono):
    def __init__(self, raio= 1):
        super().__init__(0)
        self.raio= raio

    def perimetro(self):
        c= 3.14 * 2 * self.raio
        return c

    def area(self):
        a= 3.14 * self.raio ** 2
        return a