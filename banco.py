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
    taxa = 0

    @classmethod
    def retornarCodigo(cls):
        print('Código: 555')

    @staticmethod
    def retornarCodigoBanco():
        print('Código: 345')

    # Atributos de instâncias
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero   # Visibilidade protegida (protected)
        self.titular = titular  # Visibilidade pública (public)
        self.__saldo = saldo    # Visibilidade privada (private)
        self.__historico = [saldo]

    def transacao(self, saldo):
        self.__historico.append(saldo)

    def saldo(self):
        self.__saldo -= Conta.taxa
        print(f'Saldo: R${self.__saldo}')

    def extrato(self):
        print("---- Extrato ----")
        print("Conta: ", self.titular)
        for saldo in self.__historico:
            print(f'Saldo: R${saldo}')

    def deposito(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)

    def saque(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)


conta1 = Conta(123, 'Vitor')
conta2 = Conta(456, 'Pedro', 5000)

conta2.transferir(700, conta1)
conta1.saldo()
conta2.saldo()
conta2.transferir(200, conta1)
conta2.extrato()

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
