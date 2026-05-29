from clases.Productos.pan import Pan

class Panaderia():
    def __init__(self, cod, nom, panes:list[Pan]):
        self.codigo = cod
        self.nombre = nom
        self.productos = panes
    
    def mis_productos(self):
        return self.productos
    
    def mi_nom(self):
        return self.nombre