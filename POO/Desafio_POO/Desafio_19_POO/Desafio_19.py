import time
from rich import print
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo= titulo
        self.paginas= paginas
        self.pagina_inicial= 1
        print(f':book: [blue]Voce acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.paginas}[/] paginas '
              f'no total. Voce agora esta na pagina [yellow]{self.pagina_inicial}[/][/]')

    def avancar_paginas(self,qnt):
        cont= 0
        for i in range(0, qnt, 1):
            if not self.final_do_livro():
                self.pagina_inicial +=1
                print(f'Pag {self.pagina_inicial} :arrow_forward:', end=' ')
                time.sleep(0.3)
                cont += 1
        print(f'[blue]Vc avancou {cont} paginas e agora esta na pagina[/] [yellow]{self.pagina_inicial}[/]')
        if self.final_do_livro():
            print(f':red_square: [red]Vc chegou ao final do livro "{self.titulo}"[/]')

    def voltar_paginas(self, qnt):
        contador= 0
        for i in range(0, qnt ,1):
            self.pagina_inicial -=1
            print(f'Pag {self.pagina_inicial} :arrow_forward:', end=' ')
            contador += 1

        print(f'Vc retornou {contador} paginas e agora esta na pagina {self.pagina_inicial}')



    def final_do_livro(self):
        if self.pagina_inicial == self.paginas:
            return True
        else:
            return False

l1= Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.voltar_paginas(2)
#l1.avancar_paginas(5)

