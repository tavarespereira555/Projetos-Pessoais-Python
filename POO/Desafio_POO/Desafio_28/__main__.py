from Classes.Classes_desafio28 import *
from rich import inspect

t= Termostato()
t.temperatura= 20.2
inspect(t, private= True, methods= True)
print(f'A temperatura atual e {t.ftemperatura}')