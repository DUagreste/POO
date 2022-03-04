from datetime import date


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    @classmethod
    def idadeNascimento(cls, nome, anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return cls(nome, idade, cpf, email)


class Medico:
    pass


"""paciente = Paciente('Pedro', 23, '000.123.321-00', 'pedro@gmail.com')
print(paciente.__dict__)
print(Paciente.idadeNascimento(1977))"""

paciente = Paciente.idadeNascimento('Pedro', 1989, '12345', 'pedro@gmail.com')
print(paciente.__dict__)
print(paciente.idade)
