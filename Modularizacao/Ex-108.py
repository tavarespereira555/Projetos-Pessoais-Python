from utilidadescev import moeda
num= float(input('Digite o preco: R$'))
print(f'O dobro de {moeda.moeda(num)} vai ser: R${moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} vai ser: {moeda.metade(num, True)}')
print(f'Aumentando 15% ficaria: R${moeda.aumentar(num, 15, True)}')
print(f'Diminuindo 10% ficaria: R${moeda.diminuir(num, 10, True)}')