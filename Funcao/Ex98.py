import time
def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas= 1
    print('-=' * 30)
    print(f'Contagem de {ini} ate {fim} de {pas} em {pas}')
    if ini < fim:
        for i in range(ini,fim + 1, pas):
            print(i, end=' ')
            time.sleep(0.5)
        print('FIM!!')
    else:
        for item in range(ini, fim  - 1, - pas):
            print(item, end=' ')
            time.sleep(0.5)
        print('FIM!!')
"""
if ini < fim:
    pos = ini
    while pos <= fim:
        print(pos, end=' ')
        pos += 1
else:
    pos= ini
    while pos >= fim: pos = 10 fim = 0
        print(pos, end=' ')
        pos -= 1
        """
contador(1,10 ,1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora e sua vez de personalizar a contagem!')
Inicio= int(input('Inicio: '))
Fim= int(input('Fim: '))
Passo= int(input('Passo: '))
contador(Inicio, Fim, Passo)
