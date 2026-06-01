nome=str((input('Digite seu nome completo: ')))
print('O nome em \033[35mletra maiuscula\033[m fica: {}'.format(nome.upper()))
print('O nome em \033[36mletra minuscula\033[m fica: {}'.format(nome.lower()))
sem_espaco=nome.replace(' ', '')
print('A quantidade de letras \033[4;34msem espaco\033[m sera: {}'.format(len(sem_espaco)))
#print('Seu primeiro nome e {} e ele tem {} letras'.format(nome.find(' ')))
frase_cortada=nome.split()
print('O numero de letras da primeira palavra e: {}'.format(len(frase_cortada[0])))



