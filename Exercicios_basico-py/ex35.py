print('-='* 20)
print('Analisador de triangulo')
print('-=' * 20)
reta1=float(input('Reta 1: '))
reta2=float(input('Reta 2: '))
reta3=float(input('Reta 3: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Os segmentos acima \033[32mPODE\033[m formar um triangulo!!!!')
else:
    print('Os segmentos acima \033[31mNÂO PODE\033[m formar um triangulo!!!!')