class ContaBancaria:
    """
    Conta bancaria que permite fazer saques e depositos
    """
    def __init__(self,id, titular, saldo):
        self.id= id
        self._nome= titular
        self.__saldo= saldo
        print(f'Conta {self.id} criada com sucesso, __saldo atual de {self.__saldo}')

    def __str__(self) -> str:
        return f'O id {self.id} do titular {self._nome} tem {self.__saldo:5.2f} de __saldo'

    def depositar(self, valor):
        valor= abs(valor)
        self.__saldo += valor
        print(f'Deposito de {valor} na conta {self.id} autorizado')
    def sacar(self, valor):
        valor= abs(valor)
        if valor > self.__saldo:
            print(f'Saque NEGADO de {valor} na conta {self.id}')
        else:
            self.__saldo -= valor
            print(f'Saque de {valor} na conta {self.id} autorizado')
    def __getstate__(self) -> object:
        return f'Estado: id= {self.id}; nome= {self._nome}; __saldo= {self.__saldo}'