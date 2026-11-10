from rich import print
class Caneta:
    def __init__(self, cor):
        escolha= ''
        match cor.lower().strip():
            case 'azul':
                escolha= '[blue]'
            case 'vermelho ' | 'vermelho':
                escolha= '[red]'
            case 'verde':
                escolha= '[green]'
            case _:
                escolha= '[white]'
        self.cor = escolha
        self.tampada= True
    def destampar(self):
        self.tampada = False

    def escrever(self,texto):
      if self.tampada:
          print(f':prohibited: A {self.cor}caneta[/] esta tampada')
      else:
          print(f'{self.cor} {texto}[/]')

    def tampada(self):
        self.tampada= True

    def quebrar_linha(self, num):
        print('\n' * num, end='')



c1= Caneta('azul')
c1.destampar()
c1.escrever('Ola mundo')
c1.quebrar_linha(2)

c2= Caneta('verde')
c2.destampar()
c2.escrever('Faca tudo ok')
