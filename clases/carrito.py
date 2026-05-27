from clases.errores import vacioError, no_encontradoError
from clases.promociones import Promociones


class Carrito ():
    def __init__(self):
        self.total : float = 0.0 
        self.productos : list = []
        self.cant_productos : int = 0
    
     #devuelve string, tiene que decir si se agrego bien, el producto agregado y la cantidad en el carrito
    def agregarProducto(self, producto, cant:int, precio_final):
        self.productos.append((producto, cant))
        self.cant_productos += cant
        self.total += precio_final
        print(f"Producto '{producto}' fue agregado correctamente. Total de productos: {self.cant_productos} \n Sus productos: {self.productos}\n Su total: {self.total}")
        return True
                        

    def eliminarProducto(self, producto_n:str, cantidad:int, precio_final: float): #string
        try:
            encontrado = 0
            for producto, cant in self.productos:
                if producto_n == producto.mi_nombre():
                    encontrado += 1
                    if cant < cantidad:
                        raise vacioError
                    elif cant == cantidad:
                        self.productos.remove((producto, cant))
                        self.cant_productos -= cantidad
                        self.total -= precio_final * cant

                        return print(f"Producto '{producto}' fue eliminado correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.productos} \n Precio total: {self.total}")
                    else:
                        nueva_cantidad = cant - cantidad
                        self.productos.remove((producto, cant))
                        self.productos.append((producto, nueva_cantidad))
                        self.cant_productos -= cantidad
                        self.total -= precio_final * cantidad

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
    
    def mis_productos(self):
        return self.productos