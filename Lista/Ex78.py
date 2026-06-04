lista= []
lista2= []
lista3= []
for i in range(5):
    lista.append(int(input(f'Digite um valor para a posicao {i}: ')))
print('=-' * 35)
print(f'Vc digitou os numeros: {lista}')
for i in range(5):
    if max(lista) == lista[i]:
        lista2.append(i)
    if min(lista) == lista[i]:
        lista3.append(i)
print(f'O maior valor digitado foi {max(lista)} nas posicoes {'... '.join([str (num) for num in lista2])}...')
print(f'O menor valor digitado foi {min(lista)} nas posicoes {'... '.join([str (num) for num in lista3])}...')