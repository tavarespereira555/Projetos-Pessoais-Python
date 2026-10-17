times= ('Flamengo','Palmeiras',' Athletico-PR',
       'Fluminense','Bahia','Cruzeiro','Atlético-MG','Santos','Bragantino',
       'São Paulo','Coritiba','Vitória','Botafogo','Vasco','Mirassol',
       'Corinthians','Internacional','Grêmio','Remo','Chapecoense')
print(f'A) Os 5 primeiros colocados sao: {times[:5]}')
print('-' * 40)
print(f'B) Os ultimos 4 colocados da tabela sao: {times[-4:]}')
print('-' * 40)
print(f'Os times em ordem alfabetica sao: {sorted(times)}')
print('-' * 40)
print(f'D) O time da Chapecoense esta na posicao: {times.index("Chapecoense") + 1}ª')