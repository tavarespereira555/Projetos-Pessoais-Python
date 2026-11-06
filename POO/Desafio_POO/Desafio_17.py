from rich.panel import Panel
from rich import print
class Produto:

    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

    def etiqueta(self):
        texto= (f'{self.nome} \n{'-'* 25}'
                f'\nR${self.preco:.^30.2f}')
        prod= Panel(texto,title='Produto')
        print(prod)

p1= Produto('Iphone 17 ', 12_500)
p1.etiqueta()
p2= Produto('Nootbook Gamer', 8_500)
p2.etiqueta()