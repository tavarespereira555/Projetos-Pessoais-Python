from Classes_009 import *
def main():
    av1= Avaliacao('Pedro', 'Matematica', 9.5)
    av1.set_nota(5)
    print(av1.__dict__)

if __name__ == '__main__':
    main()