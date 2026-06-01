km=float(input('Quantos km vc rodou?? '))
d=int(input('Quantos dias foram de aluguel do veiculo?? '))
p=d*60+0.15*km
print('O valor {}total{} a pagar e {:.2f}'.format('\033[33m', '\033[m', p))
