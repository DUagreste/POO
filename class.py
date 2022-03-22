from mimetypes import init


class Quadrado:

    def __init__(self, lado):
        self.lado = lado
        self.area = lado * lado

    def retorna_area(self):
        print(self.area)


quadrado = Quadrado(10)
quadrado.retorna_area()
