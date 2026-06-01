import random
a1=(input('Qual o nome do aluno 1?? '))
a2=(input('Qual o nome do aluno 2?? '))
a3=(input('Qual o nome do aluno 3?? '))
a4=(input('Qual o nome do aluno 4?? '))
lista=[a1,a2,a3,a4]
sorteio=random.choice(lista)
print('{}O nome escolhido foi: {}{}'.format('\033[4;36m', sorteio, '\033[m'))




