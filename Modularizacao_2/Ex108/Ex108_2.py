import Defs_108
p= float(input('Digite o preco: R$'))
print(f'A metade {Defs_108.moeda(p)} e {Defs_108.moeda(Defs_108.metade(p))}')
print(f'O dobro de {Defs_108.moeda(p)} e {Defs_108.moeda(Defs_108.dobro(p))}')
print(f'Aumentando 10% temos: {Defs_108.moeda(Defs_108.aumentar10(p))}')
print(f'Diminuindo 13% temos: {Defs_108.moeda(Defs_108.dimi13(p))}')