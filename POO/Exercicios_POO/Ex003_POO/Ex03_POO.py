class ContaBancaria:
    """
    Conta bancaria que permite fazer saques e depositos
    """
    def __init__(self,id, titular, saldo):
        self.id= id
        self.nome=titular
        self.saldo= saldo
        print(f'Conta {self.id} criada com sucesso, saldo atual de {self.saldo}')

    def __str__(self) -> str:
        return f'O id {self.id} do titular {self.nome} tem {self.saldo:5.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de {valor} na conta {self.id} autorizado')
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de {valor} na conta {self.id}')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} na conta {self.id} autorizado')
    def __getstate__(self) -> object:
        return f'Estado: id= {self.id}; nome= {self.nome}; saldo= {self.saldo}'

c1= ContaBancaria(112, 'Paulo', 5000)
c1.depositar(1000)
c1.sacar(500)
print(c1)
print(c1.__doc__)
print(c1.__getstate__())
print(c1.__dict__)