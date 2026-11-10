from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qnt_lados= 0):
        self.lados= qnt_lados

    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass