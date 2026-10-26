def metade(n, forma= False):
    met= n / 2
    if forma:
        met= f'R${float(met):5.2f}'
    return met
def dobro(n, forma= False):
    dobr= n * 2
    if forma:
        dobr= f'R${dobr:5.2f}'
    return dobr
def aumentar10(n, taxa= 10, forma= False):
    aumen= n + (n * taxa / 100)
    if forma:
        aumen= f'R${aumen:5.2f}'
    return aumen
def dimi13(n, taxa= 13, forma= False):
    dimi= n - (n * taxa / 100)
    if forma:
        dimi= f'R${dimi:5.2f}'
    return dimi
def moeda(n):
    n= f'R${n:5.2f}'
    return n