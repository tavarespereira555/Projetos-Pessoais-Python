import time
def maior(* num):
    cont = Mair = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i}', end=' ')
        time.sleep(0.5)
        if cont == 0:
            Mair= i
        else:
            if i > Mair:
                Mair= i
        cont += 1
    print(f'foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi: {Mair}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(2,1)
maior(6)
maior()