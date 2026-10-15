lista= ('Pao', 'queijo', 'batata frita', 'refrigerante',
        'Viajar', 'corrida', 'academia', 'musica', 'premio',
        'coberta', 'agua', 'beber', 'amigos', 'frio', 'celular')
vogais= 'a', 'e', 'i', 'o', 'u'
if vogais in lista:
    for item in lista:
        print(f'Na palavra {item}  temos: {vogais}')