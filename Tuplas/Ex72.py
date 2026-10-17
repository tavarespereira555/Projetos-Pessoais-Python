contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        leitura = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= leitura <=20:
            break
        print('Tente novamente. ', end= '')
    print(f'Vc digitou o numero {contagem[leitura]}')
    continu= str(input('Deseja continuar: [S/N] '))
    if continu in 'Nn':
        break
