
def metade(n, forma):
    num= n / 2
    if forma:
        num= f'{num:.2f}'.replace(".", ",")
    return num
def dobro(n, forma):
    Num= n * 2
    if forma:
        Num= f'{Num:.2f}'.replace(".", ",")
    return Num
def aumentar(n, taxa, forma):
    num= n + (n * taxa / 100)
    if forma:
        num= f'{num:.2f}'.replace(".", ",")
    return num
def diminuir(n, taxa, forma):
    num= n - (n * taxa / 100)
    if forma:
        num= f'{num:.2f}'.replace(".", ",")
    return num
def moeda(n):
    num= f'{n:.2f}'.replace(".",",")
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