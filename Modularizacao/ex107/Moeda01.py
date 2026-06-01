
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

