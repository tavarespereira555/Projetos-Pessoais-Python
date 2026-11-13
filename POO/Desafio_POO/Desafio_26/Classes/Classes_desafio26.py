from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print
class Funcionario(ABC):
    def __init__(self,nome, sal_bruto, salario):
        self.nome= nome
        self.sal_bruto= sal_bruto
        self.salario= salario
        self.sal_min= 1612
        self.inss= 7.5 / 100

    def analisar_sal(self):
        a, b = self.calc_sal()
        conteudo= f'O salario de [blue]{self.nome}[/] [purple]({type(self).__name__})[/]'
        conteudo += f' e de [green]{a}[/] e corresponde a [yellow]{b} salarios minimos[/]'
        mostrar= Panel(conteudo, title='Analise de salarios', width=50)
        print(mostrar)

    @abstractmethod
    def calc_sal(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self,nome= '',valor_hora= 1, horas_trab= 1, sal_bruto= 1, salario= 1):
        super().__init__(nome, sal_bruto, salario)
        self.nome= nome
        self.valor_hora= valor_hora
        self.horas_trab= horas_trab

    def calc_sal(self):
        sal= self.horas_trab * self.valor_hora
        desconto= sal * self.inss
        valorf_sal= sal - desconto
        valorf_sal_forma= f'R${valorf_sal:.2f}'
        minimo= valorf_sal / self.sal_min
        minimo_forma= f'{minimo:.1f}'
        return valorf_sal_forma, minimo_forma


class FuncionarioMensalista(Funcionario):
    def __init__(self,nome= '', sal_bruto= 1, salario= 1):
        super().__init__(nome, sal_bruto, salario)
        self.nome= nome
        self.sal_bruto= sal_bruto

    def calc_sal(self):
        desconto= self.sal_bruto * self.inss
        valorfinal= self.sal_bruto - desconto
        valorfinal_forma= f'R${valorfinal:.2f}'
        qnt_sal_min= valorfinal / self.sal_min
        qnt_sal_min_forma= f'{qnt_sal_min:.1f}'
        return valorfinal_forma, qnt_sal_min_forma
