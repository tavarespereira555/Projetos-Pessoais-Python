listagem= ('Lapis', 1.75, 'Borracha', 2.50, 'Caderno', 15.90,
           'Estojo', 30, 'Transferidor', 4.20, 'Compasso', 9.99,
           'Mochila', 120.40, 'Canetas', 16.90, 'Livro', 50.55)
print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)
for i in range (0, len(listagem), 2):
    print(f'{listagem[i]:.<30} R${listagem[i + 1]:>7.2f}')
print('-' * 40)