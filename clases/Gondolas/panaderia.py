from clases.Productos.pan import Pan

class Panaderia():
    def __init__(self, cod, nom, panes:list[Pan]):
        self.codigo = cod
        self.nombre = nom
        self.productos = panes