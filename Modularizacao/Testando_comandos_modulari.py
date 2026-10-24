def fatorial(n):
    f= 1
    for i in range(1, n+1):
        f *= i
    return f
num= int(input('Digite um numero: '))
resp= fatorial(num)
print(f'O fatorial de {num} e {resp}')