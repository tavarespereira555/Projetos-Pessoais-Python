def fatorial(n):
    f= 1
    for i in range(1, n + 1):
        f *= i
    return f
if __name__ == '__main__':
    num= int(input('Digete um numero: '))
    v_retornado= fatorial(num)
    print(f'O fatorial do numero {num} vai ser: {v_retornado}')