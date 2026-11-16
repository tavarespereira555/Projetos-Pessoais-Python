from abc import ABC, abstractmethod
import random
from random import randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.golpe = ''
        self.forca = ''
        self.nome= nome
        self.vida= vida
        self.golpes= []

    def atacar(self, alvo, forca):
        self.forca= forca
        for i, v in enumerate(self.golpes):
            print(f'{i}- {v}')
        escolha= int(input(f'Escolha o golpe: '))
        match escolha:
            case 0:
                self.golpe= self.golpes[0]
            case 1:
                self.golpe= self.golpes[1]
            case 2:
                self.golpe= self.golpes[2]
        if self.vida > 0 and alvo.vida > 0:
            #golpe= random.choice(self.golpes)
            print(f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com uma {self.golpe} de forca {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def receber_dano(self, dano):
        fator= randint(0, dano)
        self.vida= self.vida - fator
        if self.vida < 0:
            self.vida= 0

        print(f'[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]')

    @abstractmethod
    def curar(self):
        pass

    def status_jogo(self):
        print(f'{self.nome} -> {self.vida} pontos de vida com as opcoes de golpes: {self.golpes} com forca de {self.forca}')



class Guerreiro(Personagem):
    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.golpes= ['Soco', 'Pulo Giratorio', 'Golpe de machado']


    def curar(self):
        cura= random.randint(0, 100)
        self.vida += cura
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida')



class Mago(Personagem):
    def __init__(self, nome , vida):
        super().__init__(nome, vida)
        self.golpes= ['Raio de luz', 'Bola de fogo', 'Magia estatica']

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f'[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida')