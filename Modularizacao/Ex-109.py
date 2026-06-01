from utilidadescev import moeda
n= float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(n)} vai ser {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} vai ser {moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(n, 13, True)}')
