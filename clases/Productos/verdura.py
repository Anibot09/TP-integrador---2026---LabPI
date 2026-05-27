from clases.Productos.producto import Producto

class Verdura(Producto):
    def __init__(self, cod, nom, marca, price, st, st_min, peso):
        super().__init__(cod, nom, marca, price, st, st_min)
        self.peso = peso
    
    def mi_precio(self)-> float:
        return self.precio
    
    def mi_codigo(self)-> int:
        return self.codigoBarra
    
    def mi_peso(self)-> int:
        return self.peso
    
    def mi_nombre(self)-> str:
        return self.nombre
    
    def mi_marca(self)-> str:
        return self.marca
    
    def mi_stock(self):
        return self.stock
    
    def mi_stock_min(self):
        return self.stock_min
    
    def modif_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        return
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio}"