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
                        

    def eliminarProducto(self, producto_n:str, cantidad:int): #string
        try:
            encontrado = 0
            for producto, cant in self.productos:
                if producto_n == producto.mi_nombre():
                    encontrado += 1
                    precio_final = producto.mi_precio()
                    stock = producto.mi_stock()
                    if cant < cantidad:
                        raise vacioError
                    elif cant == cantidad:
                        self.productos.remove((producto, cant))
                        self.cant_productos -= cantidad
                        self.total -= precio_final * cant
                        producto.modif_stock(stock - cant)
                        print(f"Producto '{producto}' fue eliminado correctamente. \n Total de productos: {self.cant_productos}\n Sus productos: ")
                        for nombre, cant in self.productos:
                            print(f"-{self.productos} \n Precio total: {self.total}")
                        return
                    else:
                        nueva_cantidad = cant - cantidad
                        self.productos.remove((producto, cant))
                        self.productos.append((producto, nueva_cantidad))
                        self.cant_productos -= cantidad
                        self.total -= precio_final
                        producto.modif_stock(stock - cant)
                        
                        return print(f"Cantidad ingresada del '{producto}' fue eliminada correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.productos} \n Precio total: {self.total}")
            
            else:
                encontrado +=0
            
            if encontrado == 0:
                raise no_encontradoError
        
        except no_encontradoError:
            print("Producto no encontrado")
            return 0
    
    def actualizar_Total(self, nuevo_total): #float
        self.total = nuevo_total
        print(f"Su nuevo total con promociones aplicadas es:{self.total}")
    
    def ver_promociones(self, promos, gondolas):
        promociones = promos.mis_promos()
        for gondola in gondolas:
            for producto in gondola.mis_productos():
                if producto.mi_codigo() in promociones:
                    promo = promociones[producto.mi_codigo()]
                    print(f"{promo['producto']} tiene promo {promo['promo']} en marca {promo['marca']}")
                else:
                    print("Actualmente no encontramos ningún producto con promoción")
        
    def ver_promociones_producto(self, promos, gondolas, producto_nom):
        encontrado = 0
        promociones = promos.mis_promos()
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        codigo = producto.mi_codigo()
                        if codigo in promociones:
                            promo = promociones[codigo]
                            print(f"{promo['producto']} tiene promo {promo['promo']} en marca {promo['marca']}")
                        else:
                            print("Actualmente ese producto no cuenta con ninguna promoción.")
            if encontrado == 0:
                raise no_encontradoError
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")

    
    def mis_productos(self):
        return self.productos