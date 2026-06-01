
def metade(n, forma= False):
    '''
    :param n:
    :param forma:
    :return:
    '''
    num= n / 2
    return num if not forma else moeda(num)
def dobro(n, forma= False):
    Num= n * 2
    if forma:
        Num= f'{Num:.2f}'.replace(".", ",")
    return Num
def aumentar(n, taxa, forma=False):
    num= n + (n * taxa / 100)
    if forma:
        num= f'{num:.2f}'.replace(".", ",")
    return num
def diminuir(n, taxa, forma=False):
    num= n - (n * taxa / 100)
    if forma:
        num= f'{num:.2f}'.replace(".", ",")
    return num
def moeda(n, sifra='R$'):
    num= f'{sifra}{n:.2f}'.replace(".",",")
    return num
def resumo(n, aumen, dimi):
    print('-' * 28)
    print('       RESUMO VALOR')
    print('-' * 28)
    print(f'Preco Analisado: R${moeda(n)}')
    print(f'Dobro do preco: R${dobro(n, True)}')
    print(f'Metade do preco: R${metade(n, True)}')
    print(f'{aumen}% de aumento: R${aumentar(n, aumen, True)}')
    print(f'{dimi}% de reducao: R${diminuir(n, dimi, True)}')
    print('-' * 28)