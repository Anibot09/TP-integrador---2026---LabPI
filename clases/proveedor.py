from clases.Productos.producto import Producto
from clases.deposito import Deposito
from clases.pedido import Pedido

class Proveedor:
    def __init__(self, nom: str, cont: str):
        self.nombre = nom
        self.contacto = cont 
    
    def recibirPedido_reposicion(self, pedido: Pedido, deposito : Deposito): 
        prod = pedido.mi_producto()
        cant = pedido.mi_cantidad()
        deposito.agregar_producto(prod, cant)
        return
    
    def enviarReposicion(): 
        pass