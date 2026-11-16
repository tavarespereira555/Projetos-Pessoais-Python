from rich import inspect, print


class Diario:
    def __init__(self, senha):
        self.__segredos= []
        self.__senha= senha


    def escrever(self, msg):
        self.msg= msg
        self.__segredos.append(msg)

    def ler(self, senha= 'Cev12'):
        self.senha= senha
        try:
            if senha == self.__senha:
                print('[green]Diario liberado[/]')
                for i in range(len(self.__segredos)):
                    print(f'- {self.__segredos[i]}')
        except:
            print('Senha invalida!! Voce não pode ler meu diario')

d= Diario('Pular')
d.escrever('Lindo dia')
d.escrever('Belos cabelos')
d.escrever('Opaa')
d.ler()
inspect(d, private= True, methods= True)
