from rich import inspect, print
from POO.Exercicios_POO.Ex05_Poo.Classes_05 import *


a1= Aluno('Joao', 18, 'Informatica', 'B')
inspect(a1)
a1.fazer_aniversario()
a1.fazer_matricula()
p1= Professor('Samuel', 32, 'Quimica', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()
f1= Funcionario('Matilda', 31, 'Secretaria', 'Secretaria')
f1.fazer_aniversario()
f1.bater_ponto()