from clases.Productos.carne import Carne
class Carniceria():
    def __init__(self, cod, nom, carnes:list[Carne]):
        self.codigo = cod
        self.nombre = nom
        self.productos = carnes