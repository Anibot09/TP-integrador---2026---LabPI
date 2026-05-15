from producto import Producto

class Verdura(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min, peso):
        super().__init__(cod, nom, marca, price, st, st_min)
        self.peso = peso