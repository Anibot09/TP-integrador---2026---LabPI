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
        return producto.calcular_precio(cant)
            
    def calcular_promociones(self, carrito):#recibe el precio previemente determinado y de haber promocion la calcula
        total = 0.0

        precio_bebidas = 0.0
        precio_galletitas = 0.0
        precio_perfumes = 0.0

        cant_galletitas = 0
        cant_bebidas = {}
        cant_perfumes = 0


        for producto, cant in carrito.mis_productos(): #recorre mi lista de tuplas (el carrito)
            precio_unitario = producto.mi_precio() 
            tipo = producto.mi_tipo()
            marca = producto.mi_marca()

            #-----2x1 en galles
            if tipo == "galletita":
                cant_galletitas += cant
                if cant_galletitas >= 2:
                    if cant_galletitas % 2 == 0:
                        precio_galletitas = (cant_galletitas/2)*precio_unitario 
                    else:
                        precio_galletitas = ((cant_galletitas//2)+1)*precio_unitario #división de enteros //
                else:
                    precio_galletitas += precio_unitario
                total += precio_galletitas

            #-------30% en bebidas
            elif tipo == "bebida":
                if marca not in cant_bebidas:
                    cant_bebidas[marca] = cant
                else:
                    cant_bebidas[marca] += cant

                for marca, cantidad in cant_bebidas.items():
                    if cantidad >= 2:
                        if cantidad % 2 == 0: 
                            precio_bebidas = (cantidad / 2) * (precio_unitario + (precio_unitario - (precio_unitario * 0.30)))
                        else:
                            sobrantes = cantidad % 2
                            precio_bebidas = (cantidad // 2) * (precio_unitario + (precio_unitario - (precio_unitario * 0.30))) + sobrantes * precio_unitario
                else:
                    precio_bebidas += precio_unitario * cant
                precio_bebidas += total
                
            #-------50% en perfume
            elif tipo == "perfumeria":
                cant_perfumes += cant
                precio_perfumes = precio_unitario * 0.50 * cant
                precio_perfumes += total

            #no hay promo
            else:
                precio_spromo = self.determinar_precio(producto, cant)
                total += precio_spromo
        
        return total
    

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
                    #lo encuentro
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        prod = producto
                        #chequeo stock
                        if cant <= producto.mi_stock(): # chequea que haya stock suficiente
                            precio_base = self.determinar_precio(producto, cant)
                            carrito.agregarProducto(producto, cant, precio_base)
                            self.actualizar_stock(producto, cant, "restar")
                            total_promo = self.calcular_promociones(carrito)
                            carrito.actualizar_Total(total_promo)
                            agregado +=1
                            return True
                        #sin stock
                        else:
                            agregado += 0
                    #no encontro
                    else:
                        encontrado += 0
            #no encontro    
            if encontrado == 0:
                raise no_encontradoError
            #no stock
            if agregado == 0:
                raise vacioError        
        #entra al no stock
        except vacioError:
                print("Producto sin stock! Por favor espere a que repongamos e intente agregarlo de vuelta")
                if inventario.reponerInternamente(prod, cant) == False:
                    pedido = inventario.generarPedido(prod, cant)
                    self.contactar_proveedor(pedido, proveedor, dep)
                    inventario.reponerInternamente(prod, cant)#quizas innecesario/ preguntar el viernes
                else: 
                    print("Ya repusimos ingrese su compra de vuelta.")
                return False  
        #entra al no encontrado      
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")
                return False


#devuelve bool
    def monitorear_eliminacion(self, producto, cant, carrito: Carrito):
        
        if carrito.mis_productos() == []:
            print("Su carrito se encuentra vacío! Por favor agregue articulos para eliminar.")
            return False
        else:
            carrito.eliminarProducto(producto, cant)
            total_promo = self.calcular_promociones(carrito)
            carrito.actualizar_Total(total_promo)
            return True
    

    