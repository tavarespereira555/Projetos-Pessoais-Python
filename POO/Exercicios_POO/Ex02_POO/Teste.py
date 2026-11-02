#Declaracao de classe
class gafanhoto:
    def __init__(self):
        #Atributo de instancia
        self.nome= ''
        self.idade= 0


    #Metodos de instancia
    def aniversario(self):
        self.idade= self.idade + 1

    def mensagem(self):
        return f'{self.nome} e um gafanhoto(a) e tem {self.idade} anos de idade'


#Declaracao de objetos
g1= gafanhoto()
g1.nome= 'Paulo'
g1.idade= 23
print(g1.mensagem())

g2= gafanhoto()
g2.nome= 'Katia'
g2.idade= 12
g2.aniversario()
print(g2.mensagem())

g3= gafanhoto()
g3.nome= 'Lucas'
g3.idade=54
print(g3.mensagem())