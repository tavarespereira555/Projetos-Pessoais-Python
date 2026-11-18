from Classes.Classes_desafio28 import *
from rich import inspect
def main():
    try:
        t= Termostato()
        t.temperatura= 20.2
        inspect(t, private= True, methods= True)
    except Exception as e:
        print(f'Houve um problema {e}')
    print(f'A temperatura atual e {t.ftemperatura}')
if __name__ == '__main__':
    main()