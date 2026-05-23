from clases.errores import vacioError
from clases.Gondolas import * 

class Carrito ():
    def __init__(self, gondolas: dict):
        self.total : float = 0.0 
        self.list_productos : list
        self.cant_productos : int = 0
        self.gondolas = gondolas
    
     #devuelve string, tiene que decir si se agrego bien, el producto agregado y la cantidad en el carrito
    def agregarProducto(self, producto:str, cant:int):
        # verificacion de  que producto se refiere
        #verif gondola
        #gondola = self.gondolas[]
        try:
            #if producto in gondola:
            #    raise vacioError
            #elif cant > stock:
            #    raise vacioError
            #else:
                self.list_productos.append(producto)
                self.cant_productos += cant
                self.total += precio * cant
    
                return f"Producto '{producto}' fue agregado correctamente. Total de productos: {self.cant_productos} \n Sus productos {self.list_productos}"
        except vacioError:
            print("Actualmente no tenemos ese producto, por favor espere para que repongamos")

    def eliminarProducto(self, producto:str, precio:float, cant:int): #string

        self.list_productos.remove(producto)
        self.cant_productos -= cant
        self.total -= precio * cant

        return f"Producto '{producto}' fue eliminado correctamente. Total de productos: {self.cant_productos}\n Sus productos: {self.list_productos} \n Precio total: {self.total}"
    
    def calcularTotal(self): #float
        pass