from rich.panel import Panel
from rich import print
class Churrasco:
    def __init__(self, titulo,quanti):
        self.titutlo= titulo
        self.quanti= quanti
        self.peso= 0.4
        self.preco= 82.40
        self.kg= self.peso * self.quanti
        self.custotot= self.preco * self.kg
        self.custope= self.custotot / self.quanti
    
    def analisar(self):
        texto= (f'Analisando [green]{self.titutlo}[/] com [blue]{self.quanti} convidados[/]'
                f'\nCada participante comera {self.peso}Kg e cada Kg custara R${self.preco:.2f}'
                f'\nRecomendo [blue]comprar {self.kg:.3f}Kg[/] de carne'
                f'\nO custo total sera de [green]R${self.custotot:.2f}[/]'
                f'\nCada pessoa pagara [yellow]R${self.custope:.2f}[/] para participar')
        prod= Panel(texto, title=self.titutlo)
        print(prod)
    def __str__(self) -> str:
        pass
    def __getstate__(self) -> object:
        pass


c1= Churrasco('Churras dos primos', 15)
c1.analisar()