from clases.Productos.carne import Carne
class Carniceria():
    def __init__(self, cod, nom, carnes:list[Carne]):
        self.codigo = cod
        self.nombre = nom
        self.productos = carnes
    
    def mis_productos(self):
        return self.productos