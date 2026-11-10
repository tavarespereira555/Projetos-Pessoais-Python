from rich import print
class Funcionario:
    #Atributos de classe
    empresa= 'Curso em video'
    def __init__(self, nome, setor, cargo):
        #Atributos de instancia
        self.nome= nome
        self.setor= setor
        self.cargo= cargo

    def __str__(self) -> str:
        pass
    def apresentar(self):
        return (f':handshake:Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da'
                f' Empresa {Funcionario.empresa}#ou self.__class__.empresa')


f1= Funcionario('Pedro', 'TI', 'Programador')
print(f1.apresentar())
f2= Funcionario('Maria', 'Administracao', 'Diretoria')
print(f2.apresentar())