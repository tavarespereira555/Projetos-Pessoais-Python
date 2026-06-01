n1=float(input('Digite o numero: '))
n2=float(input('Digite o numero: '))
n3=float(input('Digite o numero: '))
menor= n1
if n2 < n1 and n2 <n3:
    menor= n2
if n3 < n1 and n3 < n2:
    menor= n3
maior= n1
if n2 > n3 and n2 > n1:
    maior= n2
if n3 > n1 and n3 > n2:
    maior= n3
print('O \033[32mmaior\033[m numero sera {}'.format(maior))
print('O \033[31mmenor\033[m numero sera {}'.format(menor))