turma = {}
for i in range(1):
    turma['Nome']= str(input('Nome: '))
    turma['Media'] = float(input(f'Media de {turma['Nome']}: '))
    if turma['Media'] >= 7:
        turma['Situacao'] = 'Aprovado'
    elif 5 <= turma['Media'] < 7:
        turma['Situacao'] = 'Recuperacao'
    elif 0 <= turma ['Media'] < 5: # ou else
        turma['Situacao'] = 'Reprovado'
print('=-' * 35)
for k, v in turma.items():
    print(f'\t-{k} é igual a {v}')
