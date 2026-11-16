from abc import ABC, abstractmethod
class Transporte(ABC):
    def __init__(self,distancia= 1, peso= 1):
        self.distancia= distancia
        self.peso= peso
        self.frete= 0

    @abstractmethod
    def calc_frete(self):
        pass



class Moto(Transporte):
    fator= 0.5
    def __init__(self,distancia= 1, peso= 1):
        super().__init__(distancia, peso)
        self.multiplicador= 1
    def calc_frete(self):
        if self.peso <= 10:
            self.multiplicador= Drone.fator * 1.5
        elif 20 > self.peso > 10:
            self.multiplicador= Drone.fator * 2.5
        elif 20 < self.peso < 30:
            self.multiplicador=Drone.fator * 3.5
        else:
            return f'Limite excedendo a carga maxima'
        self.frete= self.distancia * Moto.fator + self.multiplicador
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator= 1.2

    def __init__(self,distancia= 1, peso= 1):
        super().__init__(distancia, peso)
        self.multiplicador= 1
    def calc_frete(self):
        if self.peso <= 200:
            self.multiplicador= Caminhao.fator * 1.5
        elif 600 > self.peso > 200:
            self.multiplicador= Caminhao.fator * 2.5
        elif 600 < self.peso < 1000:
            self.multiplicador= Caminhao.fator * 3.5
        else:
            return f'Limite excedendo a carga maxima'

        if self.distancia < 50:
            return (f'Raio minimo de 50 km.')
        else:
            self.frete= self.distancia * self.fator + self.multiplicador
            return f'R${self.frete:.2f}'


class Drone(Transporte):
    fator= 9.5

    def __init__(self,distancia= 1, peso= 1):
        super().__init__(distancia, peso)
        self.multiplicador= 1
    def calc_frete(self):
        if self.peso <= 10:
            self.multiplicador= Drone.fator * 1.5
        elif 20 > self.peso > 10:
            self.multiplicador= Drone.fator * 2.5
        elif 20 < self.peso < 30:
            self.multiplicador=Drone.fator * 3.5
        else:
            return f'Limite excedendo a carga maxima'
        if self.distancia > 10:
            return (f'Raio maximo de 10Km')
        self.frete= self.distancia * Drone.fator + self.multiplicador
        return f'R${self.frete:.2f}'
