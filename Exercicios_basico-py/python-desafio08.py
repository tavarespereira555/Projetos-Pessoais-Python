valor=float(input('Digite o valor em metro: '))
km=valor/1000
hm=valor/100
dam=valor/10
dm=valor*10
cm=valor*100
mm=valor*1000
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(valor,km,hm,dam,dm,cm,mm))

