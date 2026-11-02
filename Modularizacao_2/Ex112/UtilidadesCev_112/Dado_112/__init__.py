def leiadinheiro(n):
    while True:
        num = (input(n)).replace(',', '.')
        try:
            valor= float(num)
        except ValueError:
            print('\033[31mErro! Digite apenas numeros validos\033[m')
        else:
            return valor


#    if num != float:
#       print('Erro digite apenas numero valido')