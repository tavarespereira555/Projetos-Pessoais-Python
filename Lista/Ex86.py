lista= []
#0, 1, 2
#3, 4, 5
#6, 7, 8
for l in range(3):
    for c in range(3):
        num= int(input(f'Digite um valor para a posicao {[l,c]}:'))
        lista.append(num)
print('=-' * 35)
for i,v in enumerate(lista):
    print(f'[\t{v}\t]',  end='')
    if i % 3 == 2:
        print()

