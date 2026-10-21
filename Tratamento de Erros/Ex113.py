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
def leiaFloat(m):
    try:
        n= float(m)
    except:
        print('\033[31mERRO!!! Digite apenas numero real validos\033[m')
    return n
n= leiaInt('Digite um numero Inteiro: ')
num= leiaFloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {num}')