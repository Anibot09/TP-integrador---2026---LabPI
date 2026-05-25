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
        agregado = 0
        encontrado = 0
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        if cant <= producto.mi_stock(): # chequea que haya stock suficiente
                            self.productos.append((producto, cant))
                            self.cant_productos += cant
                            stock = producto.mi_stock()
                            stock -= cant
                            if almacen.calcular_promociones(producto, cant) == 0:
                                precio = almacen.determinar_precio(producto, cant)
                            else:
                                precio = almacen.calcular_promociones(producto, cant)
                            self.total += precio
                            agregado += 1
                            print(f"Producto '{producto}' fue agregado correctamente. Total de productos: {self.cant_productos} \n Sus productos: {self.productos}\n Su total: {self.total}")
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
            print("Actualmente no tenemos ese producto, por favor espere para que repongamos")
            #almacen.monitorear_compra()
        except no_encontradoError:
            print("Producto no encontrado")
            return 0

    def eliminarProducto(self, producto_nom:str, cantidad:int, almacen : Almacen): #string
        try:
            encontrado = 0
            for producto, cant in self.productos:
                if producto_nom == producto.mi_nombre():
                    encontrado += 1
                    if cant < cantidad:
                        raise vacioError
                    elif cant == cantidad:
                        self.productos.remove((producto, cant))
                        self.cant_productos -= cantidad
                        if almacen.calcular_promociones(producto, cantidad) == 0:
                            precio = almacen.determinar_precio(producto, cantidad)
                        else:
                            precio = almacen.calcular_promociones(producto, cantidad)
                        self.total -= precio * cant

                        return print(f"Producto '{producto}' fue eliminado correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.productos} \n Precio total: {self.total}")
                    else:
                        nueva_cantidad = cant - cantidad
                        self.productos.remove((producto, cant))
                        self.productos.append((producto, nueva_cantidad))
                        self.cant_productos -= cantidad
                        if almacen.calcular_promociones(producto, cantidad) == 0:
                            precio = almacen.determinar_precio(producto, cantidad)
                        else:
                            precio = almacen.calcular_promociones(producto, cantidad)
                        self.total -= precio * cantidad

                        return print(f"Cantidad ingresada del '{producto}' fue eliminada correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.productos} \n Precio total: {self.total}")
            else:
                encontrado +=0
            
            if encontrado == 0:
                raise no_encontradoError
        
        except no_encontradoError:
            print("Producto no encontrado")
            return 0
    
    #def calcularTotal(self): #float
    #    pass