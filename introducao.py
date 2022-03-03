"""
Paradigma Imperativo - Fortran - Sequência, Decisão e Iteração
Paradigma Estruturado - C - Structs
Paradigma Procedural - Python
"""

# Paradigma imperativo


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

-------------------------------------------
Conceitos Estruturais

- Classe
É uma estrutura que abstrai um conjunto de objetos com características
similares. Definindo o comportamento dos seus objetos através das
estruturas.:

1- Atributos
2- Métodos

A classe define um tipo de dado abstrato.
"""

# Reuso e Coesão: sempre focar nisso
# Acoplamento, Herança, Polimorfismo, GAP semântico

"""
Conceitos Fundamentais

- Abstração
Processo pelo qual se isolam atributos de um objeto, considerando
os que certos grupos de objetos tem em comum.

- Reúso
Não existe pior prática em programação do que repetir código.
"""
