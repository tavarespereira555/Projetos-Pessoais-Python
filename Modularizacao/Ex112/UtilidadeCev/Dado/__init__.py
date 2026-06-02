def leia_dinheiro(num):
    valido= False
    while not valido:
        entrada = str(input(num)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" e um preco invalido!!!!\03[m')
        else:
            valido= True
            return float(entrada)