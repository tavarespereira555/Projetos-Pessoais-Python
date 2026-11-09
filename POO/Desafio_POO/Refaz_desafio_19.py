from rich import print
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo= titulo
        self.paginas_tot= paginas
        self.paginas_atual= 1
        print(f':book: [blue]Voce acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.paginas_tot}[/] paginas '
            f'no total. Voce agora esta na pagina [yellow]{self.paginas_atual}[/][/]')


    def avancar_paginas(self, qnt):
        cont= 0
        for i in range(0, qnt,1):
            if not self.final_livro():
                self.paginas_atual += 1
                print(f'Pag {self.paginas_atual} ', end='')
                cont+= 1
        print(f'Vc avancou {cont} paginas e agora esta na pagina {self.paginas_atual}')
        if self.final_livro():
            print(f':red_square: [red]Vc chegou ao final do livro "{self.titulo}"[/]')

    def final_livro(self):
        if self.paginas_atual == self.paginas_tot:
            return True
        else:
            return False


l1= Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)