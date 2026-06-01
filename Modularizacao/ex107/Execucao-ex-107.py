from Modularizacao.ex107 import Moeda01
num= float(input('Digite o preco: R$'))
print(f'O dobro de R${num} vai ser: R${Moeda01.dobro(num, True)}')
print(f'A metade de R${num} vai ser: R${Moeda01.metade(num, True)}')
print(f'Aumentando 10% fica: R${Moeda01.aumentar(num, 10, True)}')
print(f'Diminuindo 13% fica: R${Moeda01.diminuir(num, 13,True)}')






















