lanche= ('hamburguer', 'suco', 'Pizza', 'pudim', 'Batata frita')
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
for cont in range(len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi demais')
for posi, comi in enumerate(lanche):
    print(f'Vou comer {comi} na posicao {posi}')
#del apaga a variavel