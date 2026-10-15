contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    leitura = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= leitura <=20:
        print(f'Vc digitou o numero {contagem[leitura]}')
        break
    print('Tente novamente. Digite um numero entre 0 e 20')
