a1= float(input('Digite o primeiro termo da P.A: '))
r= float(input('Digite a razao dessa P.A:  '))
for i in range(10):
    Tot= a1 + i * r
    print(f'{i + 1}° termo {Tot}')