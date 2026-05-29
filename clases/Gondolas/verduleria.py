from clases.Productos.verdura import Verdura
class Verduleria():
    def __init__(self, cod, nom, verduras:list[Verdura]):
        self.codigo = cod
        self.nombre = nom
        self.productos = verduras
        
    def mis_productos(self):
        return self.productos
    
    def mi_nom(self):
        return self.nombre