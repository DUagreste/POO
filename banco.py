"""
Visibilidade = modificador de acesso
privada (private) - restrita -> atributos e métodos só podem ser manipulados //
dentro da classe.
protegida (protected) - intermediária -> atributos e métodos só podem ser //
manipulados dentro da classe e das classes herdadas.
pública (public) - irrestrito -> atributos e métodos são acessíveis em //
qualquer lugar.
"""


class Conta:

    # Atributos de classe
    taxa = 0.50

    @classmethod
    def retornarCodigo(cls):
        print('Código: 555')

    @staticmethod
    def retornarCodigoBanco():
        print('Código: 345')

    # Atributos de instâncias
    def __init__(self, numero, titular, saldo):
        self._numero = numero   # Visibilidade protegida (protected)
        self.titular = titular  # Visibilidade pública (public)
        self.__saldo = saldo    # Visibilidade privada (private)

    def extrato(self):
        self.__saldo -= Conta.taxa
        print(f'Saldo: R${self.__saldo}')

    def deposito(self, valor):
        self.__saldo += valor
        print("Transação efetuada com sucesso!")

    def saque(self, valor):
        self.__saldo -= valor
        print("Transação efetuada com sucesso!")


"""# Instâncias da Classe Conta
conta1 = Conta(1, 'Maria Silva', 5000)
conta2 = Conta(2, 'Paulo Santos', 2000)

print(conta1.__dict__)
print(conta2.__dict__)

conta1.extrato()

# Atributo Dinâmico -> Criado na execução
conta2.carro = 'fiat uno'

print(conta1.__dict__)
print(conta2.__dict__)

del conta2.carro

print(conta1.__dict__)
print(conta2.__dict__)

# Método da Classe
Conta.retornarCodigo()  # Convenção
conta1.retornarCodigo()

# Método Estático
Conta.retornarCodigoBanco()  # Convenção
conta2.retornarCodigoBanco()
"""
