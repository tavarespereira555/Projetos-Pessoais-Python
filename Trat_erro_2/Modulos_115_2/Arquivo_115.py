def leiaInt(msg):
    while True:
        try:
            n1= int(input(msg))
        except ValueError:
            print('\033[31mERRO!!! Digite apenas numero inteiro validos\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não informar o dado\033[m')
            return 0
        else:
            return n1

c= ('\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[107m'         # 6 - branco
    )


def titulo(msg, cor= 0):
    print(linha(50))
    print(c[cor], end='')
    print(f'{msg.center(50)}')
    print(linha(50))
    print(c[0], end='')

def menu(lista):
    titulo('Menu Principal')
    c= 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha(50))
    opc= leiaInt('Sua Opcao: ')
    return opc


def linha(tam= 50):
    return '-' * tam
