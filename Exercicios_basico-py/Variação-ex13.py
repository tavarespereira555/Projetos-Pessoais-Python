Valor=float(input('Digite o valor do produto: R$'))
vista=Valor-(Valor*10/100)
prazo=Valor+Valor*5/100
print('Um produto pago a vista ganha 10% de desconto e o mesmo produto pago a prazo tem 5% de aumento\nentão um produto que custa {:.2f} pagando a vista ele sai por {:.2f} e pagando a prazo fica {:.2f}'.format(Valor,vista,prazo))


