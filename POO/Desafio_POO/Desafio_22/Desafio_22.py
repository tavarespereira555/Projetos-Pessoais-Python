from rich import print
from rich.panel import Panel
class ControleRemoto:
    canal_min:int=1
    canal_max:int= 6
    volume_min:int= 1
    volume_max:int= 5
    def __init__(self, canal =1, volume= 2):
        self.canal_atual:int= canal
        self.volume_atual:int= volume
        self.ligado:bool= False

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual= ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1


    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1


    def liga_desliga(self):
        self.ligado= not self.ligado

    def mostrar_tv(self):
        conteudo= ''
        if not self.ligado:
            conteudo= ':prohibited: [red]A TV esta desligada[/]'
        else:
            conteudo ='CANAL  ='
            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if self.canal_atual == c:
                    conteudo += f'[yellow on yellow] {c} [/]'
                else:
                    conteudo += f' {c}'
            conteudo += f'\nVOLUME = '
            for vol in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if vol <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'
        tv= Panel(conteudo, title= '[ TV ] ', width=30  )
        print(tv)
c1= ControleRemoto(1,3)
while True:
    c1.mostrar_tv()
    comando= str(input(f'< CH{c1.canal_atual} >  - VOL{c1.volume_atual} + '))
    match comando:
        case 0:
            break
        case '@':
            c1.liga_desliga()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()
        case '-':
            c1.volume_menos()
        case '+':
            c1.volume_mais()
    print(f'\n' * 10)
