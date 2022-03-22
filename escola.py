class Aluno:

    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.matricula = matricula
        self.notas = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


aluno1 = Aluno("Vitor", 22, 123456)
print(aluno1.nome)
aluno1.nome = "João"
print(aluno1.idade)
print(aluno1.nome)
