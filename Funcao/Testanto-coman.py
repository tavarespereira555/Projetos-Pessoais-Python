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



"""#LISTA
valores= [22,43,21,56,78,95]
def dobrar(lst):
    pos= 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(valores)
dobrar(valores)"""



"""def teste(b):
    a= 8
    b += 5
    c= 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a= 5
teste(a)
print(f'A fora vale {a}')"""
#------------------------------------------------
"""def fatorial(num= 1):
    f= 1
    for i in range(num, 0,-1):
        f *= i
    return f

f1= fatorial(5)
f2= fatorial(10)
print(f'Os fatorias dos valores são: {f1} e {f2}')"""

def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False

n1= int(input('Digite um numero: '))
if par(n1):
    print('E PAR')
else:
    print('E IMPAR')