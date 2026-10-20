import datetime
def voto(num= 0):
    #anoAtual= datetime.date.today().year
    idade= datetime.date.today().year - num
    if 65 >= idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATORIO ')
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif idade > 65 or 18 > idade >=16:
        print(f'Com {idade} anos: VOTO OPCIONAL')


print('-' * 30)
ano= int(input('Em que ano vc nasceu?? '))
voto(ano)