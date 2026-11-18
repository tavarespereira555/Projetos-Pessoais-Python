from rich import print, inspect


class Credencial:
    def __init__(self):
        self.senha= ''
        self.__hash= ''


    def validar(self, chave= ''):
        self.chave= chave
        if chave == self.senha:
            print('Senha confere!!')
            return print(f'[green]{True} [/]')
        else:
            print('Senha nao bate!!')
            return False


c= Credencial()
c.senha= 'Cev'
#print(c.validar('Cev'))
inspect(c, private= True, methods= True)