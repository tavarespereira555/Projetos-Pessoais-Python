lista= ('Pao', 'queijo', 'batata frita', 'refrigerante',
        'Viajar', 'corrida', 'academia', 'musica', 'premio',
        'coberta', 'agua', 'beber', 'amigos', 'frio', 'celular')
vogais= ('a', 'e', 'i', 'o', 'u')
for palavra in lista:
    print(f'Na palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
    print()
