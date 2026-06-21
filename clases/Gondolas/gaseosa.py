from clases.Productos.liquido import Liquido
class GondolaGaseosa():
    def __init__(self, cod, nom, bebidas:list[Liquido], cant_p):
        self.codigo = cod
        self.nombre = nom
        self.productos = bebidas
        self.cant_p = cant_p
        
    def mis_productos(self):
        return self.productos
    
    def mi_nom(self):
        return self.nombre
    
    def mi_cantidad(self):
        return self.cant_productos
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.cant_p += nueva_cantidad