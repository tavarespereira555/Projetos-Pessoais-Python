import math
angulo=float(input('Qual o valor do angulo: '))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tg=math.tan(math.radians(angulo))
print('O angulo {} possui o {}cosseno{} {:.3f}\nO angulo {} possui o  {}seno{} {:.3f}\nO angulo {} possui a {}tangente{} igual a {:.3f}'.format(angulo,'\033[4;33m', '\033[m', cosseno, angulo, '\033[4;34m', '\033[m',seno,angulo, '\033[4;35m', '\033[m', tg))
