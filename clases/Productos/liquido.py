from clases.Productos.producto import Producto

class Liquido(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min, lit):
        super().__init__(cod, nom, marca, price, st, st_min)
        self.cant_litros = lit
        
    def mi_precio(self)-> float:
        return self.precio
    
    def mi_codigo(self)-> int:
        return self.codigoBarra
    
    