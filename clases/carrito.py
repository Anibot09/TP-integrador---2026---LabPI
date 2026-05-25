from clases.errores import vacioError, no_encontradoError
from clases.Gondolas import * 
from clases.almacen import Almacen

class Carrito ():
    def __init__(self, gondolas: list):
        self.total : float = 0.0 
        self.productos : list = []
        self.cant_productos : int = 0
        self.gondolas = gondolas
    
     #devuelve string, tiene que decir si se agrego bien, el producto agregado y la cantidad en el carrito
    def agregarProducto(self, producto_nom:str, cant:int, almacen : Almacen):
        #verif gondola
        gondolas = self.gondolas
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    if producto_nom == producto.mi_nombre():
                        if cant <= producto.mi_stock():
                            self.productos.append(producto)
                            self.cant_productos += cant
                            stock = producto.mi_stock()
                            stock -= cant
                            if almacen.calcular_promociones(producto, cant) == 0:
                                precio = almacen.determinar_precio(producto, cant)
                            else:
                                precio = almacen.calcular_promociones(producto, cant)
                            self.total += precio
                            enc =+ 1
                            print(f"Producto '{producto}' fue agregado correctamente. Total de productos: {self.cant_productos} \n Sus productos: {self.productos}\n Su total: {self.total}")
                            return True
                    else:
                        enc = 0
                        #raise vacioError
                else:
                    enc = 0
                    #raise no_encontradoError
        except vacioError:
            print("Actualmente no tenemos ese producto, por favor espere para que repongamos")
            #almacen.monitorear_compra()
        except no_encontradoError:
            print("Producto no encontrado")
            return 0

    def eliminarProducto(self, producto:str, cant:int, almacen : Almacen): #string

        self.list_productos.remove(producto)
        self.cant_productos -= cant
        if almacen.calcular_promociones() == 0:
            precio = almacen.determinar_precio()
        else:
            precio = almacen.calcular_promociones()
        self.total -= precio * cant

        return f"Producto '{producto}' fue eliminado correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.list_productos} \n Precio total: {self.total}"
    
    def calcularTotal(self): #float
        pass