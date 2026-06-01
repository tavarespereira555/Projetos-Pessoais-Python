import random
import time

print('Vou pensar em um numero entre a e 5. Tente adivinhar...')

g= random.randint(0, 5) #randint(0,5)
n1=int(input('Tenta adivinha o numero entre 0 e 5: '))
print('Processando...')
time.sleep(3)
if n1 == g:
    print('\033[32mVc venceu!!!\033[m MEUS PARABÉNS')
else:
    print('\033[31mVc perdeu!!!\033[m Eu pensei no numero {} e não no {}'.format(g, n1))
