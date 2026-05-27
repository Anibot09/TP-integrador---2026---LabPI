from clases.deposito import Deposito
from clases.pedido import Pedido
from clases.Gondolas import *
from clases.errores import no_encontradoError


class Inventario():
    def __init__(self, num, dep: Deposito, gond:list):
        self.num = num
        self.deposito = dep
        self.gondolas = gond
    
    def ubicarProducto(productos: list)->str:
        pass
    
    def chequearDisponibilidad(self, producto):
        try:
            encontrado = 0
            for gondola in self.gondolas:
                    for producto in gondola.mis_productos():
                        if producto.mi_stock() <= producto.mi_stock_min():
                            encontrado += 1
                            return 0
                        else:
                            return 1
            if encontrado == 0:
                raise no_encontradoError
        
        except no_encontradoError:
            print("Producto no encontrado")
            return 2
    
    def generarPedido(self, producto, cant)->Pedido:
        if self.deposito.reponer_producto(producto, cant) == 0:
            pedido = Pedido(producto, cant)
            return pedido
    
    def reponerInternamente(self, producto, cant):
        productos = []
        if self.chequearDisponibilidad(producto) == 0:
            if self.deposito.reponer_producto(producto, cant)== 0:
                return False
                #print("pedido")
            else:
                productos = self.deposito.reponer_producto(producto, cant)
                self.ubicarProducto(productos)
                print("Se pudo reponer correctamente.")
                return True
    
            
    