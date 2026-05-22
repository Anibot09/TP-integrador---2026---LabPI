from clases.Productos.producto import Producto

class Verdura(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min):
        super().__init__(cod, nom, marca, price, st, st_min)
    
    def mi_precio(self)-> float:
        return self.precio