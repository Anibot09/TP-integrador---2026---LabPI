from clases.deposito import Deposito
from clases.pedido import Pedido
from clases.Gondolas import *
from clases.errores import no_encontradoError


class Inventario():
    def __init__(self, num, dep: Deposito, gond:list):
        self.num = num
        self.deposito = dep
        self.gondolas = gond
    
    def ubicarProducto(self, producto)->str: #falta actualizar cantidad, recibe list [producto, cant]
        codigo = producto.mi_codigo()
        for gondola in self.gondolas:
            # Carnicería
            if isinstance(producto, Carne) and "Carniceria" in gondola.nombre:
                gondola.mis_productos().append(producto)
                gondola.cant_productos += 1
                break

            # Panadería
            elif isinstance(producto, Pan) and "Panaderia" in gondola.nombre:
                gondola.mis_productos().append(producto)
                gondola.cant_productos += 1
                break

            # Verdulería
            elif isinstance(producto, Verdura) and "Verduleria" in gondola.nombre:
                gondola.mis_productos().append(producto)
                gondola.cant_productos += 1
                break

            # Gaseosas
            elif isinstance(producto, Liquido) and "Gaseosas" in gondola.nombre:
                gondola.mis_productos().append(producto)
                gondola.cant_productos += 1
                break

            # Productos grales(Perfumería, Galletitas, Electro, Juguetes)
            elif isinstance(producto, Producto_gral):
                if 600 <= codigo <= 699 and "Perfumeria" in gondola.nombre:
                    gondola.mis_productos().append(producto)
                    gondola.cant_productos += 1
                    break
                elif 700 <= codigo <= 799 and "Galletitas" in gondola.nombre:
                    gondola.mis_productos().append(producto)
                    gondola.cant_productos += 1
                    break
                elif 800 <= codigo <= 899 and "Electro" in gondola.nombre:
                    gondola.mis_productos().append(producto)
                    gondola.cant_productos += 1
                    break
                elif 900 <= codigo <= 999 and "Juguetes" in gondola.nombre:
                    gondola.mis_productos().append(producto)
                    gondola.cant_productos += 1
                    break

        return print("Productos ubicados correctamente.")
    
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
    
            
    