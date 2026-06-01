cidade= str((input('Qual o nome da sua cidade??? '))).strip().lower()
cidade_cortada= cidade.split()[0]
resultado= cidade_cortada == 'santo' or cidade_cortada == 'santos'
print('Comeca com {}Santo{}? {}'.format('\033[4;36m', '\033[m', resultado))