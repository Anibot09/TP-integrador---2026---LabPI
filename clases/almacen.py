from clases.Productos.carne import Carne
from clases.Productos.pan import Pan
from clases.Productos.verdura import Verdura
from clases.Productos.liquido import Liquido
from clases.promociones import Promociones
from clases.carrito import Carrito
from clases.inventario import Inventario
from clases.proveedor import Proveedor
from clases.pedido import Pedido
from clases.deposito import Deposito
from clases.errores import vacioError, no_encontradoError

class Almacen():
    def __init__(self, num, promos: Promociones, gond: list):
        self.num_id = num
        self.promociones = promos
        self.gondolas = gond
       
    def determinar_precio(self, producto, cant):#Toma en cuenta cantidades y peso para determinar precios de ciertos productos. 
        if type(producto)== Carne: #Carnes
            precio = producto.mi_precio()
            peso = producto.mi_peso()
            precio_final = (peso*precio)*cant
            return precio_final
        elif type(producto)== Pan:#Panes
            precio = producto.mi_precio()
            bol = producto.mis_bolsones()
            precio_final = (precio*bol)*cant
            return precio_final
        elif type(producto)== Verdura:#Verduras
            precio = producto.mi_precio()
            peso = producto.mi_peso()
            precio_final = (peso*precio)*cant
            return precio_final
        #elif type(producto)== Liquido:#Bebidas
        #    precio = producto.mi_precio()
        #    litros = producto.mi_litro()
        #    precio_final = (litros*precio)*cant
        #    return precio_final
        else:
            precio = producto.mi_precio()
            precio_final = precio*cant
            return precio_final
        
            
    def calcular_promociones(self, producto, cant, precio):#recibe el precio previemente determinado y de haber promocion la calcula
        promociones = self.promociones.mis_promos()
        precio_unitario = producto.mi_precio()
        if producto.mi_codigo() in promociones:
            promo = promociones[producto.mi_codigo()] 
            if promo['promo'] == "2x1":
                if cant>=2:
                    if cant % 2 == 0:
                        precio_final = (cant/2)*precio_unitario 
                    else:
                        precio_final = ((cant//2)+1)*precio_unitario #división de enteros //
                    return precio_final
                else:
                    print("No hay cantidad necesaria para agregar el descuento.")
                    return precio
            elif promo["promo"] == "30 descuento(2da/misma marca)":
                if cant>=2:
                    if cant % 2 == 0:
                        precio_final = (cant/2)*(precio_unitario + (precio_unitario-(precio_unitario*0.30)))
                    else:
                        sobrantes = cant % 2
                        precio_final = (cant//2)*(precio_unitario + (precio_unitario-(precio_unitario*0.30))) + sobrantes*precio
                    return precio_final
                else:
                    print("No hay cantidad necesaria para agregar el descuento.")
                    return precio
            elif promo["promo"] == "50 descuento":
                precio_final = precio*0.50
                return precio_final
        else:
            #("Producto sin promoción")
            return precio
    
    def actualizar_stock(self, producto, cant, operacion):
        stock_actual = producto.mi_stock()
        if operacion == "restar":
            producto.modif_stock(stock_actual - cant)
        elif operacion == "sumar":
            producto.modif_stock(stock_actual + cant)

    def contactar_proveedor(self, pedido : Pedido, proveedor : Proveedor, dep : Deposito):
        proveedor.recibirPedido_reposicion(pedido, dep)
        return
        
    
    def monitorear_compra(self, producto_nom, cant, carrito: Carrito, inventario: Inventario, proveedor : Proveedor, dep : Deposito): #chequea que el estado de los productos y gondolas al  realizar la compra
        gondolas = self.gondolas
        agregado = 0
        encontrado = 0
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        if cant <= producto.mi_stock(): # chequea que haya stock suficiente
                            precio_base = self.determinar_precio(producto, cant)
                            precio_final = self.calcular_promociones(producto, cant, precio_base)
                            carrito.agregarProducto(producto, cant, precio_final)
                            self.actualizar_stock(producto, cant, "sumar")
                            agregado +=1
                            return True
                        else:
                            agregado += 0
                    else:
                        encontrado += 0
                
            if encontrado == 0:
                raise no_encontradoError
            if agregado == 0:
                raise vacioError        
            
        except vacioError:
                print("Actualmente no tenemos ese producto, por favor espere para que repongamos. Intente agregarlo de vuelta")
                if inventario.reponerInternamente(producto, cant) == False:
                    pedido = inventario.generarPedido(producto, cant)
                    self.contactar_proveedor(pedido, proveedor, dep)
                    inventario.reponerInternamente(producto, cant)#quizas innecesario/ preguntar el viernes
                else: 
                    print("Ya repusimos ingrese su compra de vuelta.")
                return False        
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")
                return False
            
    def monitorear_eliminacion(self, producto, cant, carrito: Carrito, inventario: Inventario):
        if carrito.mis_productos() == []:
            print("La lista se encuentra actualmente vacía, por favor agregue articulos para eliminar.")
            return False
        else:
            precio_base = self.determinar_precio(producto, cant)
            precio_final = self.calcular_promociones(producto, cant, precio_base)
            carrito.eliminarProducto(producto, cant, precio_final)
            self.actualizar_stock(producto, cant, "restar")
            return True
    

    