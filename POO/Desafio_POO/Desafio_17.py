from rich.panel import Panel
from rich import print
class Produto:

    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

    def etiqueta(self):
        texto= f'{self.nome.center(30, " ")}'
        texto += f' \n{'-'* 30}'
        precof= f'R${self.preco:.2f}'
        texto += f'\n{precof.center(30, ".")}'
        prod= Panel(texto,title='Produto', width=34)
        print(prod)

p1= Produto('Iphone 17 ', 12_500)
p1.etiqueta()
p2= Produto('Nootbook Gamer', 8_500)
p2.etiqueta()