def fatorial(n1, show):
    f= 1
    if show == False:
        for i in range(n1, 0,-1):
            f *= i
    else:
        for i in range(n1, 0,-1):
            f *= i
            print(f'{i} x', end=' ')
        print(f'= {f}')
    return f


fatorial(5,show=True)
