import random
a1=(input('Qual o nome do aluno 1?? '))
a2=(input('Qual o nome do aluno 2?? '))
a3=(input('Qual o nome do aluno 3?? '))
a4=(input('Qual o nome do aluno 4?? '))
lista=[a1,a2,a3,a4]
#random.shuffle(lista)
# print(lista)
nova_lista=random.sample(lista,k=len(lista))
print('A ordem de \033[31mapresentaçao\033[m vai ser')
print(nova_lista)


