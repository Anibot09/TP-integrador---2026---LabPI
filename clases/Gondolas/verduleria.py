from clases.Productos.verdura import Verdura
class Verduleria():
    def __init__(self, cod, nom, verduras:list[Verdura]):
        self.codigo = cod
        self.nombre = nom
        self.productos = verduras