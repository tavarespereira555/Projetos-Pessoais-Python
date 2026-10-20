def leiaInt(msg):
    while True:
        n1= (input(msg))
        if n1.isnumeric():
            n1= int(n1)
            return n1
        else:
            print('\033[31mERRO! Digite apenas um numero inteiro valido.\033[m')


n= leiaInt('Digite um numero: ')
print(f'Vc acabou de digitar o numero {n}')