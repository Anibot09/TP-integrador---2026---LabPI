
class Gondola():
    def __init__(self, cod, nom:str, productos:list, cant_p):
        self.codigo = cod
        self.nombre = nom
        self.list_productos = productos
        self.cant_productos = cant_p
    
    def mis_productos(self):
        return self.list_productos