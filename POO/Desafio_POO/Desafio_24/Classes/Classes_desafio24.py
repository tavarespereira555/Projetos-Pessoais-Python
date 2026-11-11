from abc import ABC, abstractmethod


class Cafeteria(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print('--- Iniciando o preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f'--- Bebida Pronta ---')



    def ferver_agua(self):
        print(f'1. Fervendo a agua em 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass


class Cafe(Cafeteria):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print(f'2. Passando a agua pressurizada pelo pó de cafe moído.')

    def servir(self):
        print(f'3. Servindo em xicara pequena')


class Cha(Cafeteria):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print(f'2. Mergulhando o sache de ervas na agua')

    def servir(self):
        print(f'3. Servindo na caneca de porcelana com limao')


class Leite(Cafeteria):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print(f'2. Passando o vapor pressurizado pelo bico do leite')

    def servir(self):
        print(f'3. Servindo na caneca grande, ja com cafe')
