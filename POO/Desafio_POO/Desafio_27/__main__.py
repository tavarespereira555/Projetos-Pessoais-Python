from Classes.Classes_desafio27 import *

p1= Guerreiro('Kratos', 2000)
p2= Mago('Merlin', 3000)
p1.atacar(p2, 1500)
p2.atacar(p1, 200)
p1.curar()
p2.curar()
p1.status_jogo()
p2.status_jogo()
