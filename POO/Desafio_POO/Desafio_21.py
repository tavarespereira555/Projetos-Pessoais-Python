from rich import print
class Caneta:
    def __init__(self, cor):
        self.cor= cor
    def destampar(self):
        pass
    def escrever(self,texto):
        if self.cor == 'vermelho':
            print(f'[red]{texto}[/]')
        if self.cor == 'verde':
            print(f'[green] {texto}[/]')
        if self.cor == 'azul':
            print(f'[blue] {texto}[/]')

    def quebrar_linha(self, num):
        q= num * '\n'
        return q



c1= Caneta('azul')
c1.escrever('Ola mundo')
c1.destampar()

c2= Caneta('verde')
c2.escrever('Faca tudo ok')
