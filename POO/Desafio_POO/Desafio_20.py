from rich.panel import Panel
from rich import print
class Gamer:
    def __init__(self,nome, nick):
        self.nome= nome
        self.nick= nick
        self.favoritos= []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos= sorted(self.favoritos, key=str.lower)
    def ficha(self):
        texto= f'Nome real: [black on blue] {self.nome} [/]'
        texto +=f'\nJogos favoritos: '
        for i in self.favoritos:
            texto += f'[blue]\n:video_game: {i}[/]'

        prod= Panel(texto,title=f'Jogador <{self.nick}>', width=40)
        print(prod)


j1= Gamer('Pedro', 'Nanico')
j1.add_favoritos('Mario bros')
j1.add_favoritos('Gta 5')
j1.add_favoritos('Cs go')
j1.add_favoritos('Raft')
j1.ficha()
