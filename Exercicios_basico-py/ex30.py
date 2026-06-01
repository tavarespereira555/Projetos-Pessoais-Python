num=int(input('Qual o numero? '))
resultado= num % 2
if resultado == 0:
    print('O numero {} e \033[32mPAR\033[m!!!'.format(num))
else:
    print('O numero {} e \033[31mIMPAR\033[m!!!'.format(num))