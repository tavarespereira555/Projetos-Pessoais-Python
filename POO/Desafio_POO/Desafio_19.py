import time
from rich import print
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo= titulo
        self.paginas= paginas
        self.pagina_inicial= 1
        print(f':book: [blue]Voce acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.paginas}[/] paginas '
              f'no total. Voce agora esta na pagina [yellow]{self.pagina_inicial}[/][/]')

    def avancar_paginas(self,qnt):
        if self.pagina_inicial + qnt > self.paginas:
            qnt= self.paginas - self.pagina_inicial# 20 - 6
        for i in range(self.pagina_inicial + 1,self.pagina_inicial + qnt + 1):
            print(f'Pag {i} :arrow_forward:', end=' ')
            time.sleep(0.5)
        self.pagina_inicial += qnt
        print(f'[blue]Vc avancou {qnt} paginas e agora esta na pagina[/] [yellow]{self.pagina_inicial}[/]')
        if self.pagina_inicial == self.paginas:
            print(f':red_square: [red]Vc chegou ao final do livro {self.titulo}[/]')
l1= Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(20)

