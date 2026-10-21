def leiaInt(msg):
    ok= False
    valor= 0
    while True:
        n1= str(input(msg))
        if n1.isnumeric():
            valor= int(n1)
            ok= True
        else:
            print('\033[31mERRO!!! Digite apenas numero inteiro validos\033[m')
        if ok:
            break
    return valor

n= leiaInt('Digite um numero: ')
print(f'Vc acabou de digitar o numero {n}')