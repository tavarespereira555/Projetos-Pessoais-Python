def metade(n, forma= False):
    met= n / 2
    #if forma:
        #met= f'R${float(met):5.2f}'
    return met if forma is False else moeda(met)
def dobro(n, forma= False):
    dobr= n * 2
    #if forma:
        #dobr= f'R${dobr:5.2f}'
    return dobr if forma is False else moeda(dobr)
def aumentar10(n, taxa= 10, forma= False):
    aumen= n + (n * taxa / 100)
    #if forma:
        #aumen= f'R${aumen:5.2f}'
    return aumen if forma is False else moeda(aumen)
def dimi13(n, taxa= 13, forma= False):
    dimi= n - (n * taxa / 100)
    #if forma:
        #dimi= f'R${dimi:5.2f}'
    return dimi if forma is False else moeda(dimi)
def moeda(n, sifra= 'R$'):
    n= f'{sifra}{n:5.2f}'
    return n

