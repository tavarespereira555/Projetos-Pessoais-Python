num=int(input('Digite um numero entre 0 a 9999: '))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print('A \033[33munidade\033[m do numero e: {}'.format(u))
print('A \033[33mdezena\033[m do numero e: {}'.format(d))
print('A \033[33mcentena\033[m do numero e: {}'.format(c))
print('O \033[33mmilhar\033[m do numero e: {}'.format(c))