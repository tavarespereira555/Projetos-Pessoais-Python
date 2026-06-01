print('\033[36m=-\033[m' * 20)
print('Calculador de financiamento')
print('\033[36m=-\033[m' * 20)
casa= float(input('Qual o valor da casa??? '))
salario= float(input('Qual o valor do seu salario??? '))
anos= float(input('Quantos anos vc esta pensando em pagar o valor do imovel??? '))
prest= casa / (anos * 12)
print('De acordo com o tempo {}, a prestacao ira sair por {:.2f}'.format(anos, prest))
if prest < (salario * 0.30) :
    print('Como o valor do seu salario e o tempo que deseja pagar, o senhor {}esta de acordo com os termos minimos para poder iniciar o seu financiamento{} muito obrigado por preferenciar nossos seriços'.format('\033[32m', '\033[m'))
else:
    print('Como valor do seu salario e o tempo que deseja pagar, o senhor {}não esta de acordo como os termos minimos de financiamento conosco{} espero que o senhor possa compreender'.format('\033[31m', '\033[m'))