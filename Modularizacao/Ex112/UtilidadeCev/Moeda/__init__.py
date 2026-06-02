
def metade(n, forma= False):
    '''
    :param n:
    :param forma:
    :return:
    '''
    num= n / 2
    return num if not forma else moeda(num).replace('.', ',')
def dobro(n, forma= False):
    Num= n * 2
    return Num if not forma else moeda(Num).replace('.', ',')
def aumentar(n, taxa, forma=False):
    num= n + (n * taxa / 100)
    return num if not forma else moeda(num).replace('.', ',')
def diminuir(n, taxa, forma=False):
    num= n - (n * taxa / 100)
    return num if not forma else moeda(num).replace(',', '.')
def moeda(n, sifra='R$'):
    num= f'{sifra}{n:.2f}'.replace(".",",")
    return num
def resumo(n, aumen, dimi):
    print('-' * 28)
    print('RESUMO VALOR'.center(30))
    print('-' * 28)
    print(f'Preco Analisado: \t{moeda(n)}')
    print(f'Dobro do preco: \t{dobro(n, True)}')
    print(f'Metade do preco: \t{metade(n, True)}')
    print(f'{aumen}% de aumento: \t{aumentar(n, aumen, True)}')
    print(f'{dimi}% de reducao: \t{diminuir(n, dimi, True)}')
    print('-' * 28)