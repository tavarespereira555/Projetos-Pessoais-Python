frase= str((input('Qual a frase?? '))).strip().upper()
print('A frase possui {} A'.format(frase.count('A')))
print('A posicao do {}primeiro{} A na frase esta na posiçao {}'.format('\033[32m','\033[m',frase.find('A')+1))
print('A posiçao do {}ultimo{} A na frase esta na posiçao {}' .format('\033[31m','\033[m',frase.rfind('A')+1))

