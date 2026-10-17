#lista= (float(input('Digite um numero: ')), (float(input('Digite um numero:'))),
#        (float(input('Digite un numero:'))), (float(input('Digite um numero:'))))
#print(lista)
#------------------------------------------------
lista_num= []
numeros= ()
for i in range(4):
    lista_num.append((float(input(f'Digite o {i + 1} valor: '))))
numeros= tuple(lista_num)
print(f'Vc digitou os valores: {numeros}')
print(f'A) O valor 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'B) O valor 3 foi digitado na posicao: {numeros.index(3) + 1}')
else:
    print('B) O valor 3 não foi digitado em nenhuma posicao')
for item in numeros:
    if item % 2 == 0:
        print(f'C) Os valores pares digitados foram {item}')
