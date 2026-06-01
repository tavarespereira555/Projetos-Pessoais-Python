import Moeda

num= float(input('Digite o preco: R$'))
print(f'O dobro de R${num} vai ser: R${Moeda.dobro(num, True)}')
print(f'A metade de R${num} vai ser: R${Moeda.metade(num, True)}')
print(f'Aumentando 10% fica: R${Moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 13% fica: R${Moeda.diminuir(num, 13,True)}')






















