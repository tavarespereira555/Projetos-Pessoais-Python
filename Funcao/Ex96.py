def area(a, b):
    tot= a * b
    print(f'A area do \033[32mterreno\033[m {a}x{b} e de {tot}m²')

print('CONTROLE DE TERRENOS')
print('-' * 20)
base= float(input('LARGURA (m): '))
compri= float(input('COMPRIMENTO (m): '))
area(a= base,b= compri)
