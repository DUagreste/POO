# Paradigma imperativo


"""
Paradigma Imperativo - Fortran - Sequência, Decisão e Iteração
Paradigma Estruturado - C - Structs
Paradigma Procedural - Python
"""


def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente


# Paradigma Orientado à Objetos
"""
Classe - um conjunto de objeto com a mesma característica
Objeto - dado de uma classe que representa "o mundo real"
Construtor - uma função criada com mesmo nome da classe
Atributo - são variáveis de uma classe
"""


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print("Criei o objeto!")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email


"""
Simulação de eventos discretos -> POO

Relação -> Destancando funções e variáveis
"""

# Reuso e Coesão: sempre focar nisso
# Acoplamento, Herança, Polimorfismo, GAP semântico