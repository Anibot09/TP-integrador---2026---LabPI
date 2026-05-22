from clases.Productos.producto import Producto

class Carne(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min, peso):
        super().__init__(cod, nom, marca, price, st, st_min)
        self.peso = peso
        
    def mi_precio(self)-> float:
        return self.precio
    
    def mi_codigo(self)-> int:
        return self.codigoBarra
    
    def mi_peso(self)-> int:
        return self.peso