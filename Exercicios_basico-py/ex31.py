viagem= float(input('Qual a distancia da viajem?? '))
if viagem <= 200:
    valor= viagem* 0.50
    print('Com a distancia de {}Km a passagem saira por \033[31mR${:.2f}\033[m'.format(viagem,valor))
else:
    valor2= viagem * 0.45
    print('Com a distancia de {}Km a passagem saira por \033[31mR${:.2f}\033[m'.format(viagem,valor2 ))
