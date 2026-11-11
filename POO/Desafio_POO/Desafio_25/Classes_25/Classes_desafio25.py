from abc import ABC, abstractmethod
class Transporte(ABC):
    def __init__(self,distancia= 1, frete= 1):
        self.distancia= distancia
        self.frete= frete

    @abstractmethod
    def calc_frete(self):
        pass



class Moto(Transporte):
    def __init__(self,distancia= 1, frete= 1):
        super().__init__(distancia, frete)
        self.fator= 0.5

    def calc_frete(self):
        preco= self.distancia * self.fator
        preco_formatado= f'R${preco:.2f}'
        return preco_formatado

class Caminhao(Transporte):
    def __init__(self,distancia= 1, frete= 1):
        super().__init__(distancia, frete)
        self.fator= 1.20

    def calc_frete(self):
        if self.distancia < 50:
            raio= (f'Raio minimo de 50 km.')
            return raio
        else:
            preco= self.distancia * self.fator
            preco_formatado= f'R${preco:.2f}'
            return preco_formatado


class Drone(Transporte):
    def __init__(self,distancia= 1, frete= 1):
        super().__init__(distancia, frete)
        self.fator= 9.5

    def calc_frete(self):
        if self.distancia > 10:
            raio= (f'Raio maximo de 10Km')
            return raio
        preco= self.distancia * self.fator
        preco_formatado= f'R${preco:.2f}'
        return preco_formatado
