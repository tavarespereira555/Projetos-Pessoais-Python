def leia_dinheiro(letras):
    while True:
        entrada= (input(letras)).strip().replace(',', '.')
        try:
            letras1 = float(entrada)
            return letras1
        except ValueError:
            print(f'ERRO: "{entrada}" e um preco invalido')


