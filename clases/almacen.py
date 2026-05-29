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
        else:
            precio = producto.mi_precio()
            precio_final = precio*cant
            return precio_final
        
            
    def calcular_promociones(self, carrito):#recibe el precio previemente determinado y de haber promocion la calcula
        total = 0.0
        precio_total = 0.0
        precio_final = 0.0
        precio_bebidas = 0.0
        precio_galletitas = 0.0
        precio_perfumes = 0.0
        cant_galletitas = 0
        cant_bebidas = 0
        cant_perfumes = 0 
        promociones = self.promociones.mis_promos()
        for producto, cant in carrito.mis_productos(): #recorre mi lista de tuplas (el carrito)
            precio_unitario = producto.mi_precio()  #defino el precio de cada producto
            #veo si aplica alguna promo
            if producto.mi_codigo() in promociones: 
                promo = promociones[producto.mi_codigo()] 
                #2x1
                if promo['promo'] == "2x1":
                    cant_galletitas += cant
                    if cant_galletitas>=2:
                        if cant_galletitas % 2 == 0:
                            precio_final = (cant_galletitas/2)*precio_unitario 
                        else:
                            precio_final = ((cant_galletitas//2)+1)*precio_unitario #división de enteros //
                        precio_galletitas = precio_final
                    else:
                        print("No hay cantidad necesaria para agregar el descuento.")
                        precio_total  += precio_unitario
                #30%
                elif promo["promo"] == "30 descuento(2da/misma marca)":
                    cant_bebidas += cant
                    gaseosas = []
                    cant_por_marcas = {}
                    gaseosas.append((producto, cant))
                    for gaseosa, cant in gaseosas:
                        if gaseosa.mi_marca() not in cant_por_marcas:
                            cant_por_marcas[gaseosa.mi_marca()] = cant
                        else: 
                            cant_por_marcas[gaseosa.mi_marca()] += cant
                        for marca in cant_por_marcas:
                            cant = cant_por_marcas[marca]
                            if cant>=2:
                                if cant % 2 == 0:
                                    precio_final = (cant/2)*(precio_unitario + (precio_unitario-(precio_unitario*0.30)))
                                else:
                                    sobrantes = cant % 2
                                    precio_final = (cant//2)*(precio_unitario + (precio_unitario-(precio_unitario*0.30))) + sobrantes*precio
                                precio_bebidas = precio_final
                            else:
                                print("No hay cantidad necesaria para agregar el descuento.")
                                precio_total  += precio_unitario
                #50%
                elif promo["promo"] == "50 descuento":
                    cant_perfumes += cant
                    precio_final = precio_unitario*0.50
                    precio_perfumes += precio_final
            else:
                #("Producto sin promoción")
                precio_final = self.determinar_precio(producto, cant)
                precio_total += precio_final
        
        total = precio_total + precio_galletitas + precio_bebidas + precio_perfumes
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
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        prod = producto
                        if cant <= producto.mi_stock(): # chequea que haya stock suficiente
                            precio_base = self.determinar_precio(producto, cant)
                            carrito.agregarProducto(producto, cant, precio_base)
                            self.actualizar_stock(producto, cant, "sumar")
                            total_promo = self.calcular_promociones(carrito)
                            carrito.actualizar_Total(total_promo)
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
                print("Producto sin stock! Por favor espere a que repongamos e intente agregarlo de vuelta")
                if inventario.reponerInternamente(prod, cant) == False:
                    pedido = inventario.generarPedido(prod, cant)
                    self.contactar_proveedor(pedido, proveedor, dep)
                    inventario.reponerInternamente(prod, cant)#quizas innecesario/ preguntar el viernes
                else: 
                    print("Ya repusimos ingrese su compra de vuelta.")
                return False        
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")
                return False
            
    def monitorear_eliminacion(self, producto, cant, carrito: Carrito, inventario: Inventario):
        if carrito.mis_productos() == []:
            print("Su carrito se encuentra vacío! Por favor agregue articulos para eliminar.")
            return False
        else:
            carrito.eliminarProducto(producto, cant)
            total_promo = self.calcular_promociones(carrito)
            carrito.actualizar_Total(total_promo)
            return True
    

    