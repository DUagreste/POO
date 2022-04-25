guerreiro = {'for': 5, 'int': 0, 'agi': 5, 'sor': 0, 'const': 10}
mago = {'for': 0, 'int': 10, 'agi': 0, 'sor': 5, 'const': 5}
arqueiro = {'for': 5, 'int': 5, 'agi': 10, 'sor': 0, 'const': 0}
ladino = {'for': 10, 'int': 0, 'agi': 5, 'sor': 5, 'const': 0}
curandeiro = {'for': 0, 'int': 5, 'agi': 0, 'sor': 10, 'const': 5}

print(50*'-')
nome = input('Digite um nome para o personagem: ')
classe = input('''
            ---------------------------
                [ 1 ] Guerreiro
                [ 2 ] Mago
                [ 3 ] Arqueiro
                [ 4 ] Ladino
                [ 5 ] Curandeiro
            ---------------------------
            *** Escolha sua classe ***: ''')


def classe1():
    print('''
                     selecionado
                - G U E R R E I R O -''')


def classe2():
    print('''
                    selecionado
                    - M A G O -''')


def classe3():
    print('''
                    selecionado
                - A R Q U E I R O -''')


def classe4():
    print('''
                    selecionado
                  - L A D I N O -''')


def classe5():
    print('''
                      selecionado
                - C U R A N D E I R O -''')


def default():
    print("Value default")


if __name__ == "__main__":
    switch = {
        "1": classe1,
        "2": classe2,
        "3": classe3,
        "4": classe4,
        "5": classe5
    }

    case = switch.get(classe, default)
    case()

raça = input('''
            -------------------------
                [ 1 ] Humano
                [ 2 ] Elfo
                [ 3 ] Anão
                [ 4 ] Orc
            -------------------------
            *** Escolha sua raça ***: ''')


def raça1():
    print('''
                      selecionado
                    - H U M A N O -''')


def raça2():
    print('''
                      selecionado
                      - E L F O -''')


def raça3():
    print('''
                    selecionado
                    - A N Ã O -''')


def raça4():
    print('''
                    selecionado
                     - O R C -''')


def default():
    print("Value default")


if __name__ == "__main__":
    switch = {
        "1": raça1,
        "2": raça2,
        "3": raça3,
        "4": raça4
        }

    case = switch.get(raça, default)
    case()
