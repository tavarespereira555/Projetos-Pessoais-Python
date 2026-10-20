
def fatorial(n1, show= False):
    """
    -> Calcula o fatorial de um número
    :param n1: Numero a ser calculado
    :param show: (opcional) mostra ou não a contagem na tela
    :return: O valor final de um fatorial de n1
    """
    f= 1
    if show:
        for i in range(n1, 0 , -1):
            f *= i
            print(i, end='')
            if i > 1:
                print(f' x', end=' ')
            else:
                print(f'= ', end='')
    else:
        for i in range(n1, 0,-1):
            f *= i
    return f


print(fatorial(5, show= True))
help(fatorial)

