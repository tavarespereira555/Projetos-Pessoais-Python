lista= []
ListaAlun= []
while True:
    nome= str(input('Nome: '))
    lista.append(nome)
    n1= float(input('Nota 1: '))
    lista.append(n1)
    n2 = float(input('Nota 2: '))
    lista.append(n2)
    m= (n1 + n2) / 2
    lista.append(m)
    ListaAlun.append(lista[:])
    lista.clear()

    conti= str(input('Deseja continuar??? [S/N] ')).upper().strip()
    if conti == 'N':
        break
print('=-' * 40)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('----------------------------')
for i,v in enumerate(ListaAlun):
    print(f'{i:<4}{v[0]:<10}{v[-1]:>8.2f}')
print('-----------------------------------------------------')
while True:
    num= int(input('Mostrar notas de qual aluno?? (999 para parar): '))
    if num == 999:
        break
    for i, v in enumerate(ListaAlun):
        if num == i:
            print(f'Notas de {v[0]} sao {v[1], v[2]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
#lista.append([nome, [n1, n2], m])