import datetime
ano=int(input('Qual o ano??? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano= datetime.date.today().year
if ano % 4 == 0 and  ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} e \033[36mBISSEXTO\033[m!!!!'.format(ano))
else:
    print('O ano de {} \033[31mNAO E BISSEXTO\033[m!!!'.format(ano))

#if % 4 == 0 and % 100 != 0 or % 400 == 0:
    #print('Esse ano e BISSEXTO')
#import calendar
calendar.isleap(x)
#if calendar.isleap(ano)
 #print(