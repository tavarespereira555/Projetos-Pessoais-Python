from abc import ABC, abstractmethod
import random
from random import randint


class Personagem(ABC):
    def __init__(self, nome, vida , golpes):
        self.nome= nome
        self.vida= vida
        self.golpes= golpes

    def atacar(self, alvo, forca):
        num= randint(1,6)
        match num:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
        conteudo = f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com um {self.golpes} de forca'
        conteudo += f' {forca}'
        conteudo += f'\n{alvo.nome} recebeu dano de '
        print(conteudo)


    def receber_dano(self, dano):
        pass

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome= '', vida= 1000 , golpes= ''):
        super().__init__(nome, vida, golpes)
        self.nome= nome
        self.vida= vida
        self.golpes= golpes

    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome= '', vida= 1000 , golpes= ''):
        super().__init__(nome, vida, golpes)
        self.nomes= nome
        self.vida= vida
        self.golpes= golpes

    def curar(self):
        pass

p1= Guerreiro('Kratos', 2000)
p2= Mago('Merlin', 3000)
p1.atacar(p2, 1000)