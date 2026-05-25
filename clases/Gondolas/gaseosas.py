from clases.Productos.liquido import Liquido
class GondolaGaseosa():
    def __init__(self, cod, nom, bebidas:list[Liquido]):
        self.codigo = cod
        self.nombre = nom
        self.productos = bebidas
        
    def mis_productos(self):
        return self.productos