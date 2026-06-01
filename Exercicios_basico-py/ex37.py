num= float(input('Digite um numero qualquer: '))
tra= int(input('Vc quer transformar ele em binário,octal ou hexadecimal???\nPara poder transformar em binario digite 1, para octal digite 2 e para hexadecimal digite 3 '))
if tra == 1:
    print('O numero {} em tranformacao binaria ficara {}'.format(num, bin(int(num))))
elif tra == 2:
    print('O numero {} em transformacao octal sera {}'.format(num, oct(int(num))))
elif tra == 3:
    print('O numero {} em transformacao hexadecimal sera {}'.format(num, hex(int(num))))