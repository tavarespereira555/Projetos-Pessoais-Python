turma = {}
for i in range(1):
    turma['Nome']= str(input('Nome: '))
    turma['Media'] = float(input(f'Media de {turma['Nome']}: '))
    if turma['Media'] > 7:
        turma['Situcao'] = 'Aprovado'
    else:
        turma['Situcao'] = 'Reprovado'
for k, v in turma.items():
    print(f'{k} é igual a {v}')
