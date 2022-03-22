class Aluno:

    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = None


aluno1 = Aluno("Vitor", 22, 123456)
print(aluno1.nome)
print(aluno1.idade)
print(aluno1.matricula)
print(aluno1.notas)