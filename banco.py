class Conta:

    # Atributos de classe
    taxa = 0.50

    # Atributos de instâncias
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        self.saldo -= Conta.taxa
        print(f'Saldo: R${self.saldo}')

    def deposito(self, valor):
        self.saldo += valor
        print("Transação efetuada com sucesso!")

    def saque(self, valor):
        self.saldo -= valor
        print("Transação efetuada com sucesso!")


# Instâncias da Classe Conta
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
