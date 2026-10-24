def metade(n):
    met= n / 2
    return met
def dobro(n):
    return n *2
def aumentar10(n):
    aumen= n + (n * 10 / 100)
    return aumen
def dimi13(n):
    dimi= n - (n * 13 / 100)
    return dimi

preco= float(input('Digite o preço: R$'))
print(f'A metade {preco} e {metade(preco)}')
print(f'O dobro de {preco} e {dobro(preco)}')
print(f'Aumentando 10% temos: {aumentar10(preco)}')
print(f'Diminuindo 13% temos: {dimi13(preco)}')