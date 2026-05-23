from clases.deposito import Deposito
from clases.pedido import Pedido

class Inventario():
    def __init__(self, num, dep: Deposito):
        self.num = num
        self.deposito = dep
    
    def chequearDisponibilidad(self, producto):
        pass
    
    def reponerInternamente(self):
        pass 
    
    def generarPedido()->Pedido:
        pass 
    
    def ubicarProducto(Producto)->str:
        pass