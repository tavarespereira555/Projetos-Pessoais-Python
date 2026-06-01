import math
co=float(input('Digite o cateto oposto: '))
ca=float(input('Digite o cateto adjacente: '))
hipot= math.hypot(co,ca)
print('O {}cateto oposto vale {}{} e o {}cateto adjancente vale {}{} logo a {}hipotenusa vale {:.3f}{}'.format('\033[33m', co, '\033[m', '\033[34m', ca, '\033[m', '\033[36m',hipot, '\033[m'))





