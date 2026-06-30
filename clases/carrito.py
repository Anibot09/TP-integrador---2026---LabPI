from clases.errores import vacioError, no_encontradoError
from clases.promociones import Promociones


class Carrito ():
    def __init__(self):
        self.total : float = 0.0 
        self.productos : list = []
        self.cant_productos : int = 0
    

     #devuelve bool, imprime si se agrego bien, el producto agregado y la cantidad en el carrito
    def agregarProducto(self, producto, cant:int, precio_final):
        # Buscar si el producto ya existe en el carrito
        encontrado = False
        for i, (prod, cantidad) in enumerate(self.productos):
            if prod == producto:  # si coincide el nombre/objeto
                # actualizar cantidad
                nueva_cant = cantidad + cant
                self.productos[i] = (prod, nueva_cant)
                encontrado = True
                break
         # Si no estaba en el carrito, lo agregamos como nuevo
        if not encontrado:
            #guarda tuplas
            self.productos.append((producto, cant))
            #suma la cantidad al contador (podemos hacer un contador por producto)
            self.cant_productos += cant 
            #suma el precio final al total
            self.total += precio_final

        print(f"Producto '{producto}' fue agregado correctamente. Total de productos: {self.cant_productos}\n Su total: {self.total}")
        
        print("Sus productos:")
        for prod, cant in self.productos:
            print(f"- {prod} | Cantidad: {cant}")

        return True
                        

    def eliminarProducto(self, producto_n:str, cantidad:int): #recibe lo que quiere eliminar y la cantidad
        try:
            encontrado = 0
            #recorro las cosas en el carrito
            for producto, cant in self.productos:
                #si lo encuentro
                if producto_n == producto.mi_nombre():
                    encontrado += 1
                    precio_final = producto.mi_precio()
                    stock = producto.mi_stock()
                    #pero elim quiero mas de lo que hay
                    if cant < cantidad:
                        raise vacioError
                    #esta justo la cantidad que quiero eliminar
                    elif cant == cantidad:
                        self.productos.remove((producto, cant))
                        self.cant_productos -= cantidad
                        self.total -= precio_final * cant
                        producto.modif_stock(stock - cantidad)
                        
                        print(f"Producto '{producto}' fue eliminado correctamente. \n Total de productos: {self.cant_productos}")
                        
                        print("Sus productos:")
                        for prod, cant in self.productos:
                            print(f"- {prod} | Cantidad: {cant}")

                        print(f"Precio total: {self.total}")
                        
                        return
                    #si elimino solo una parte de la cantidad
                    else:
                        nueva_cantidad = cant - cantidad
                        self.productos.remove((producto, cant))
                        self.productos.append((producto, nueva_cantidad))
                        self.cant_productos -= cantidad
                        self.total -= precio_final * cantidad
                        producto.modif_stock(stock - cantidad)
                        
                        print(f"Cantidad ingresada del '{producto}' fue eliminada correctamente. Total de productos: {self.cant_productos}\n Precio total: {self.total}")
                        
                        print("Sus productos:")
                        for prod, cant in self.productos:
                            print(f"- {prod} | Cantidad: {cant}")
                        return
            
            else:
                encontrado +=0
            #si no lo encuentro
            if encontrado == 0:
                raise no_encontradoError
        #si no lo encuentro por: no en carrito
        except no_encontradoError:
            print("Producto no encontrado")
            return 0
        #o por no productos sufi en el carrito
        except vacioError:
            print("Intento eliminar más articulos de los que tiene. Por favor ingrese otra cantidad.")
            return 0
    

    def actualizar_Total(self, nuevo_total): #float
        self.total = nuevo_total
        print(f"Su nuevo total con promociones aplicadas es:{self.total}")
    

    def ver_promociones(self, promos, gondolas):
        promociones = promos.mis_promos() # obtiene el diccionario de promociones desde la clase Promociones
        
        for gondola in gondolas:
            for producto in gondola.mis_productos():
                if str(producto.mi_codigo()) in promociones:
                    promo = promociones[str(producto.mi_codigo())]
                    print(f"-{promo['producto']} tiene promo {promo['promo']}")
        

    def ver_promociones_producto(self, promos, gondolas, producto_nom):
        encontrado = 0
        promociones = promos.mis_promos()
        prod = producto_nom.lower().strip()
        #recorro las gondalas para buscar el producto
        #cambio: si ya se el tipo de producto entonces que entre directo a esa gondola
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    if prod == producto.mi_nombre():
                        encontrado += 1
                        codigo = producto.mi_codigo()
                        #obtengo el codigo y de ahi extraigo la promo (si existe)
                        if str(codigo) in promociones:
                            promo = promociones[str(codigo)]
                            print(f"-{promo['producto']} tiene promo {promo['promo']} en marca {promo['marca']}")
                        else:
                            print("Ese producto no se encuentra con promocion") 
            #si no lo encuentro
            if encontrado == 0:
                raise no_encontradoError
        #si no lo encuentro
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")


    def ver_stock_producto(self, gondolas, producto_nom):
        encontrado = 0
        
        #cambio: si ya se el tipo de producto entonces que entre directo a esa gondola
        try:
            for gondola in gondolas:
                for producto in gondola.mis_productos():
                    #cuando lo encuentro
                    if producto_nom == producto.mi_nombre():#encuentra el producto con mismo nombre
                        encontrado += 1
                        stock = producto.mi_stock()
                        print(f"Actualmente contamos con {stock} articulos de este producto.")
            #si no lo encuentro
            if encontrado == 0:
                raise no_encontradoError
        #si no lo encuentro
        except no_encontradoError:
                print("Producto no encontrado, por favor vuelva ingresarlo")

    #buenas practicas y encapsulamiento
    def mis_productos(self):
        return self.productos
    

    def mi_total(self):
        return self.total