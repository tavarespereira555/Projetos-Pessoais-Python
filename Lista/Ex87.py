lista= []
SomPar= 0
Som3Colu= 0
Ma2Lin= 0
for l in range(3):
    for c in range(3):
        num= int(input(f'Digite um valor para a posicao {[l,c]}:'))
        lista.append(num)
print('=-' * 35)
for i,v in enumerate(lista):
    print(f'[\t{v}\t]',  end='')
    if i % 3 == 2:
        Som3Colu += v
        print()
    if v % 2 == 0:
        SomPar += v
    if 3 <= i <= 5:
        if i == 3:
            Ma2Lin = v
        else:
            if v > Ma2Lin:
                Ma2Lin = v
print('=-' * 35)
print(f'Soma dos valores pares: {SomPar}')
print(f'Soma dos valores da 3 coluna: {Som3Colu}')
print(f'O maior valor da segunda linha e {Ma2Lin}')