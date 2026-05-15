from producto import Producto

class Pan(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min, peso, bolsones):
        super().__init__(cod, nom, marca, price, st, st_min)
        self.peso = peso
        self.cant_bolsones = bolsones
