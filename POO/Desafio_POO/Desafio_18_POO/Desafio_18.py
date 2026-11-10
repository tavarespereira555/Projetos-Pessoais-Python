from rich.panel import Panel
from rich import print
class Churrasco:
    consumo_padrao= 0.4
    preco_Kg= 82.40
    def __init__(self, titulo,quanti):
        self.titutlo= titulo
        self.quanti= quanti
    def calcular_quanti_carne(self):
        return Churrasco.consumo_padrao * self.quanti

    def calcular_custo_tot(self):
        return self.calcular_quanti_carne() * self.__class__.preco_Kg

    def calcular_custo_indivi(self):
        return self.calcular_custo_tot() / self.quanti

    def analisar(self):
        texto=   f'Analisando [green]{self.titutlo}[/] com [blue]{self.quanti} convidados[/]'
        texto += f'\nCada participante comera {Churrasco.consumo_padrao}Kg e cada Kg custara R${Churrasco.preco_Kg:.2f}'
        texto += f'\nRecomendo [blue]comprar {self.calcular_quanti_carne():.3f}Kg[/] de carne'
        texto += f'\nO custo total sera de [green]R${self.calcular_custo_tot():.2f}[/]'
        texto += f'\nCada pessoa pagara [yellow]R${self.calcular_custo_indivi():.2f}[/] para participar'
        prod= Panel(texto, title=self.titutlo)
        print(prod)
    def __str__(self) -> str:
        pass
    def __getstate__(self) -> object:
        pass


c1= Churrasco('Churras dos primos', 15)
c1.analisar()