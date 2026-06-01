velo=float(input('Qual a velocidade do carro?em Km/Hr '))
if velo >80:
    multa= (velo - 80)*7
    print('\033[31mVc foi multado!!!! Vc excedeu o limite permitido que era 80 Km/Hr\nE o valor da multa sera de R${:.2f}\033[m'.format(multa))
else:
    print('Parabens, vc esta de acordo com a velocidade limite!!!')
