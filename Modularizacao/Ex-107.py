
from utilidadescev import moeda


num= float(input('Digite o preco: R$'))
print(f'O dobro de R${num} vai ser: R${moeda.dobro(num, True)}')
print(f'A metade de R${num} vai ser: R${moeda.metade(num, True)}')
print(f'Aumentando 10% fica: R${moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 13% fica: R${moeda.diminuir(num, 13,True)}')






















