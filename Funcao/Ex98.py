import time
def contador(ini, fim, pas):
    print('-=' * 30)
    if ini < fim:
        print(f'Contagem de {ini} ate {fim} de {pas} em {pas}')
        for i in range(ini,fim + 1, pas):
            print(i, end=' ')
            time.sleep(0.5)
        print('FIM!!')
    else:
        print(f'Contagem de {ini} ate {fim} de {pas} em {pas}')
        for item in range(ini, fim  - 1, - pas):
            print(item, end=' ')
            time.sleep(0.5)
        print('FIM!!')


contador(1,10 ,1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora e sua vez de personalizar a contagem!')
Inicio= int(input('Inicio: '))
Fim= int(input('Fim: '))
Passo= int(input('Passo: '))
contador(Inicio, Fim, Passo)
