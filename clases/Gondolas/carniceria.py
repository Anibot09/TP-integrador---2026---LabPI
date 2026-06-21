from clases.Productos.carne import Carne
class Carniceria():
    def __init__(self, cod, nom, carnes:list[Carne], cant_p):
        self.codigo = cod
        self.nombre = nom
        self.productos = carnes
        self.cant_p = cant_p
    
    def mis_productos(self):
        return self.productos
    
    def mi_nom(self):
        return self.nombre
    
    def mi_cantidad(self):
        return self.cant_p
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.cant_p += nueva_cantidad