soma= 0
for i in range(6):
    num= int(input('Digite o numero: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos numero pares digitados foi: {soma}')