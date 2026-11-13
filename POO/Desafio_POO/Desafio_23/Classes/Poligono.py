from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qnt_lados= 0):
        self.qnt_lados= qnt_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass