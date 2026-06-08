lista= []
lista_par= []
lista_impar= []
for i in range(1, 7 + 1):
    num= int(input(f'Digite o {i}o. valor: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
lista.append(lista_par[:])
lista.append(lista_impar[:])
lista_par.sort(reverse= False)
lista_impar.sort()
print(f'Lista completa: {lista}')
print(f'Lista Par: {lista_par}')
print(f'Lista Impar: {lista_impar}')