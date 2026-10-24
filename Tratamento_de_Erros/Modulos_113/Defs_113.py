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
def leia_float(m):
    while True:
        try:
            n1 = float(input(m))
        except ValueError:
            print('\033[31mERRO!!! Digite apenas numero real valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não informar o dado\033[m')
            return 0
        else:
            return n1