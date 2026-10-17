"""
def soma(a,b ):
    s= a + b
    print(s)
    print('------------------------------')
#Programa Principal
soma(4, 5)
soma(10, 4)
soma(12, 343)
"""


"""
DESEMPACOTAMENTO
def contador( * numeros):
    somar= 0
    for num in numeros:
        somar += num
    print(f'Somando os valores {numeros} temos {somar}')
contador(5,7,6,4,3)
contador(2,3,4,5,9,6)
contador(1,2,3,4,5)
contador(1,2,3)
contador(1)
contador(1,2,3,4,5,5,8,12)
"""



#LISTA
valores= [22,43,21,56,78,95]
def dobrar(lst):
    pos= 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(valores)
dobrar(valores)


