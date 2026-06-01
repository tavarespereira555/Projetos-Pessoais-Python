import math
num=float(input('Digite um numero: '))
print('O numero {} tem a {}parte inteira{} igual a {}'.format(num, '\033[36m', '\033[m', math.trunc(num)))