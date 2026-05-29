from clases.deposito import Deposito
from clases.pedido import Pedido
from clases.Gondolas import *
from clases.errores import no_encontradoError

from clases.Productos.pan import Pan
from clases.Productos.producto_gral import Producto_gral
from clases.Productos.liquido import Liquido
from clases.Productos.carne import Carne
from clases.Productos.verdura import Verdura

class Inventario():
    def __init__(self, num, dep: Deposito, gond:list):
        self.num = num
        self.deposito = dep
        self.gondolas = gond
    
    def ubicarProducto(self, productos:list)->str: #falta actualizar cantidad, recibe list [producto, cant]
            producto = productos[0]
            cantidad = productos[1]
            codigo = productos[0].mi_codigo()
            ubicado = False 

            #producto existente
            for gondola in self.gondolas:
                #busco si existe en una gondola
                for prod_existente in gondola.mis_productos():
                    if prod_existente.mi_codigo() == codigo:
                        # Actualizar stock si ya existe (guardo ese valor en el atributo stock)
                        prod_existente.modif_stock(prod_existente.mi_stock() + cantidad)
                        print(f"Stock actualizado: {prod_existente.mi_nombre()} tiene {prod_existente.mi_stock()}")
                        ubicado = True
                        break
                if ubicado:
                    break
                #si no existe lo ubico segun tipo y gondola
            if not ubicado:
                producto.modif_stock(cantidad)
                for gondola in self.gondolas:            
                    # Carnicería
                    if isinstance(producto, Carne) and "Carniceria" in gondola.mi_nom():
                        gondola.mis_productos().append(producto)
                        gondola.actualizar_cantidad(cantidad)
                        ubicado = True
                        break

                    # Panadería
                    elif isinstance(producto, Pan) and "Panaderia" in gondola.mi_nom():
                        gondola.mis_productos().append(producto)
                        gondola.actualizar_cantidad(cantidad)
                        ubicado = True
                        break

                    # Verdulería
                    elif isinstance(producto, Verdura) and "Verduleria" in gondola.mi_nom():
                        gondola.mis_productos().append(producto)
                        gondola.actualizar_cantidad(cantidad)
                        ubicado = True
                        break

                    # Gaseosas
                    elif isinstance(producto, Liquido) and "Gaseosas" in gondola.mi_nom():
                        gondola.mis_productos().append(producto)
                        gondola.actualizar_cantidad(cantidad)
                        ubicado = True
                        break

                    # Productos grales(Perfumería, Galletitas, Electro, Juguetes)
                    elif isinstance(producto, Producto_gral):
                        if 600 <= codigo <= 699 and "Perfumeria" in gondola.mi_nom():
                            gondola.mis_productos().append(producto)
                            gondola.actualizar_cantidad(cantidad)
                            ubicado = True
                            break
                        elif 700 <= codigo <= 799 and "Galletitas" in gondola.mi_nom():
                            gondola.mis_productos().append(producto)
                            gondola.actualizar_cantidad(cantidad)
                            ubicado = True
                            break
                        elif 800 <= codigo <= 899 and "Electro" in gondola.mi_nom():
                            gondola.mis_productos().append(producto)
                            gondola.actualizar_cantidad(cantidad)
                            ubicado = True
                            break
                        elif 900 <= codigo <= 999 and "Juguetes" in gondola.mi_nom():
                            gondola.mis_productos().append(producto)
                            gondola.actualizar_cantidad(cantidad)
                            ubicado = True
                            break

            return "Productos ubicados correctamente."
    
    def chequearDisponibilidad(self, producto, cant):
        try:
            encontrado = 0
            for gondola in self.gondolas:
                for producto in gondola.mis_productos():
                    if producto.mi_stock() <= producto.mi_stock_min(): #no diponible, necesario reponer
                        encontrado += 1
                        return 0
                    elif cant > producto.mi_stock():
                        return 0 #hay stock, pero no suficiente
                    else:
                        return 1 # hay stock
            if encontrado == 0:
                raise no_encontradoError
        
        except no_encontradoError:
            print("Producto no encontrado")
            return 2 #no se encontro
    
    def generarPedido(self, producto, cant)->Pedido:
        if self.deposito.reponer_producto(producto, cant) == 0:
            pedido = Pedido(producto, cant)
            return pedido
    
    def reponerInternamente(self, producto, cant):
        productos = []
        if self.chequearDisponibilidad(producto, cant) == 0:
            productos = self.deposito.reponer_producto(producto, cant)
            if productos== 0:
                return False
            else:
                self.ubicarProducto(productos)
                print("Se pudo reponer correctamente.")
                return True
        elif self.chequearDisponibilidad(producto) == 1:
            return True
        else:
            return False
    
            
    