from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print
class Funcionario(ABC):
    salario_min= 1612
    inss= 7.5

    def __init__(self,nome):
        self.nome= nome
        self.sal_bruto= 0
        self.salario= 0

    def analisar_sal(self):
        a, b = self.calc_sal()# ou base= self.salario / Funcionario.salario_min
        conteudo= f'O salario de [blue]{self.nome}[/] [purple]({type(self).__name__})[/]'
        conteudo += f' e de [green]{a}[/] e corresponde a [yellow]{b} salarios minimos[/]'
        mostrar= Panel(conteudo, title='Analise de salarios', width=50)
        print(mostrar)
        #self.__clas__.name
    @abstractmethod
    def calc_sal(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self,nome= '',valor_hora= 7.37, horas_trab= 200):
        super().__init__(nome)
        self.nome= nome
        self.valor_hora= valor_hora
        self.horas_trab= horas_trab
        self.sal_bruto= self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario= self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
        minimo= self.salario / Funcionario.salario_min
        return f'R${self.salario:.2f}', f'{minimo:.1f}'


class FuncionarioMensalista(Funcionario):
    def __init__(self,nome= '', sal_bruto= 1612):
        super().__init__(nome)
        self.nome= nome
        self.sal_bruto= sal_bruto

    def calc_sal(self):
        self.salario= self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
        qnt_sal_min= self.salario / Funcionario.salario_min
        return f'R${self.salario:.2f}', f'{qnt_sal_min:.1f}'
