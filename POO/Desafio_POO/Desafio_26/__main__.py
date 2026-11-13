from Classes.Classes_desafio26 import *

def main():
    f1= FuncionarioHorista('Pedro', 12, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2= FuncionarioMensalista('Amanda', 9500)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == '__main__':
    main()