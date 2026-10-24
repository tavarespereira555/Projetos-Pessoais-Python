try:
    a= int(input('Numerador: '))
    b= int(input('Denominador: '))
    r= a / b

except (ValueError, TypeError):
    print('Tivemos problema com o tipo de dado que vc digitou')
except ZeroDivisionError:
    print('Não e possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar o dado')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else:
    print(f'O resultado e {r:.5f}')
finally:
    print('Volte sempre! Muito obrigado!!')