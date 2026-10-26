import Defs_109
p= float(input('Digite o preco: R$'))
print(f'A metade {Defs_109.moeda(p)} e {Defs_109.metade(p,True)}')
print(f'O dobro de {Defs_109.moeda(p)} e {Defs_109.dobro(p, True)}')
print(f'Aumentando 10% temos: {Defs_109.aumentar10(p, 10, True)}')
print(f'Diminuindo 13% temos: {Defs_109.dimi13(p, 13,True)}')