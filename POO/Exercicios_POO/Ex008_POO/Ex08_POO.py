from Classes_ex08 import *
def main():
    c1= ContaBancaria(112, 'Paulo', 5000)
    c1.depositar(-1000)
    c1.sacar(-200)
    c1.saldo= 0
    c1.nome= 'Lucas'
    print(c1.__dict__)
if __name__ == '__main__':
    main()