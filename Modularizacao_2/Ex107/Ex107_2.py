import Moeda_107

preco= float(input('Digite o preço: R$'))
print(f'A metade {preco} e {Moeda_107.metade(preco)}')
print(f'O dobro de {preco} e {Moeda_107.dobro(preco)}')
print(f'Aumentando 10% temos: {Moeda_107.aumentar10(preco)}')
print(f'Diminuindo 13% temos: {Moeda_107.dimi13(preco)}')