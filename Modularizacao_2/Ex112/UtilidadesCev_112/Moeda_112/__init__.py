
def metade(n, forma= False):
    met= n / 2
    if forma:
        met= f'R${float(met):5.2f}'
    return met.replace('.',',')
def dobro(n, forma= False):
    dobr= n * 2
    if forma:
        dobr= f'R${dobr:5.2f}'
    return dobr.replace('.',',')
def aumentar10(n, taxa= 10, forma= False):
    aumen= n + (n * taxa / 100)
    if forma:
        aumen= f'R${aumen:5.2f}'
    return aumen.replace('.', ',')
def dimi13(n, taxa= 13, forma= False):
    dimi= n - (n * taxa / 100)
    if forma:
        dimi= f'R${dimi:5.2f}'
    return dimi.replace('.',',')
def moeda(n):
    n= f'R${n:5.2f}'
    return n.replace('.', ',')
def resumo(n, taxa_aumen, taxa_dimi):
    print('-' * 30)
    print('RESUMO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: {'':8}{moeda(n)}')
    print(f'Dobro do preco: {'':9}{dobro(n, True)}')
    print(f'Metade do preco: {'':8}{metade(n, True)}')
    print(f'{taxa_aumen}% de aumento: {'':9}{aumentar10(n, taxa_aumen,True)}')
    print(f'{taxa_dimi}% de redução: {'':9}{dimi13(n,taxa_dimi,True)}')
    print('-' * 30)









#    if num != float:
#       print('Erro digite apenas numero valido')