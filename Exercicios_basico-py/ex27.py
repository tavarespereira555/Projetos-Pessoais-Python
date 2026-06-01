nome= str((input('Digite seu nome completo: '))).strip()
nome_cortado= nome.split()
print('O \033[34mprimeiro\033[m nome sera {}'.format(nome_cortado[0]))
print('O \033[33multimo\033[m nome sera {}'.format(nome_cortado[-1]))