import time
def maior(* num):
    Mair = -9999
    print('=-' * 30)
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo')
    for i in num:
        if i > Mair:
            Mair= i
    print(f'O maior valor informado foi: {Mair}')
    time.sleep(0.5)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(2,1)
maior(6)
maior()