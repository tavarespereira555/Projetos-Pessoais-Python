lista= []
while True:
    num= int(input('Digite o numero:'))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!!! Não vou adicionar')
    conti= str(input('Deseja continuar?? [S/N]')).upper().strip()
    if conti == 'N':
        break
print('=-' * 35)
lista.sort()
print(f'Voce digitou os valores {lista}')#sorted(lista)