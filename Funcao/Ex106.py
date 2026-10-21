import time

c= ('\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[107m'         # 6 - branco
    )
def ajuda(msg):
    print(f'Acessando o manual do comando \'{msg}\'')
    print(c[6], end='')
    help(msg)
    print(c[0], end='')
    time.sleep(2)

def titulo(msg, cor= 0):
    tam= len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    time.sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    n = str(input('Digite o comando > '))
    if n.upper() in 'FIM':
        break
    else:
        ajuda(n)
titulo('ATE LOGO', 1)

