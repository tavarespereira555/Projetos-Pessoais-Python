from rich import inspect, print


class Diario:
    def __init__(self, senha):
        self.__segredos= []
        self.__senha= senha


    def escrever(self, msg):
        self.msg= msg
        f'{self.__segredos.append(msg)}'

    def ler(self, senha= 'Cev12'):
        self.senha= senha
        if senha != self.__senha:
            raise ValueError('Senha invalida!! Voce não pode ler meu diario')
        else:
            print('[green]Diario liberado[/]')
            for i in range(len(self.__segredos)):
                print(f'- {self.__segredos[i]}')