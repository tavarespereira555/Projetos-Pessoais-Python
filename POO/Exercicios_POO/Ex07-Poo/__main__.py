from rich import inspect, print
from Classes import *


def main():
    a1= Aluno('Joao', 18, 'Informatica', 'B')
    #inspect(a1)
    a1.fazer_aniversario()
    a1.fazer_matricula()
    p1= Professor('Samuel', 32, 'Quimica', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    f1= Funcionario('Matilda', 31, 'Secretaria', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()