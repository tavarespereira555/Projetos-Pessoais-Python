def leia_dinheiro(letras):
    while True:
        entrada= (input(letras)).strip().replace(',', '.')
        try:
            letras1 = float(entrada)
            return letras1
        except ValueError:
            print(f'\033[31mERRO: "{entrada}" e um preco invalido!!!!\03[m')

