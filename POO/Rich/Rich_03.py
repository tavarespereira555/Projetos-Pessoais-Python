from rich import print
from rich.table import Table

tabela= Table(title='Tabela de precos')

tabela.add_column('Nome', style='blue')
tabela.add_column('Preço', style='green')
tabela.add_column('Id')
tabela.add_row('Lapis', 'R$1,50', '4')
tabela.add_row('Borracha', 'R$5,00', '6')
tabela.add_row('Caneta', 'R$3,80', '8')
print(tabela)