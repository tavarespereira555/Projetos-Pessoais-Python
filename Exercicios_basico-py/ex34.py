salario=float(input('Qual e o seu salario?? '))
if salario >= 1250.00:
    ajuste= salario* 10/100 + salario
    print('O novo valor do seu salario ja com o aumento de \033[31m10%\033[m sera de R${}'.format(ajuste))
else:
    ajuste= salario * 15/100 + salario
    print('O novo valor do seu salario com o aumento \033[31m15%\033[m sera de R${}'.format(ajuste))