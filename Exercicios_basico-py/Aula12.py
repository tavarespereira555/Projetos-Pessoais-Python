nome= str(input('Qual o seu nome?? '))
if nome == 'Thais':
    print('Seu nome e de uma pessoa muito especial')
elif nome == 'Paulo' or nome == 'Joao' or nome == 'Lucas' or nome == 'Miguel' or nome == 'Davi':
    print('Seu nome e um nome biblico')
elif nome == 'Pedro':
    print('Seu nome em ingles sera Peter')
else:
    print('Ola {}, seu nome e muito bonito'.format(nome))
print('Tenha um bom dia {}'.format(nome))

