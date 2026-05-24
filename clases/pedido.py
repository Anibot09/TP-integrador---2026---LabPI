class Pedido:
    def __init__(self, prod, cant):
        self.producto = prod
        self.cantidad = cant
        
    def mi_producto(self):
        return self.producto
    
    def mi_cantidad(self):
        return self.cantidad
    