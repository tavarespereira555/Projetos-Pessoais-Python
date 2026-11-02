#Declaracao de classe
class gafanhoto:
    """
    Essa clase cria um gafanhoto, que é uma pessoa que tem idade e nome
    para criar use:
    variavel= gafanhoto('nome', idade)
    """
    def __init__(self, n= '',i= 0):
        #Atributo de instancia
        self.nome= n
        self.idade= i


    #Metodos de instancia
    def aniversario(self):
        self.idade= self.idade + 1

    def __str__(self):
        return f'{self.nome} e um gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome= {self.nome}; idade= {self.idade}'

#Declaracao de objetos
g1= gafanhoto('Paulo', 17)
print(g1)

g2= gafanhoto('Katia', 12)
g2.aniversario()
print(g2)

g3= gafanhoto('Lucas', 54)
print(g3)

print(g1.__doc__)# Dunder
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)