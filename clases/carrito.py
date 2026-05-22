class Carrito ():
    def __init__(self, productos:list, total:float, cant_p):
        self.total = total
        self.list_productos = productos
        self.cant_productos = cant_p
    
     #devuelve string, tiene que decir si se agrego bien, el producto agregado y la cantidad en el carrito
    def agregarProducto(self, producto:str, precio:float, cant:int):

        self.list_productos.append(producto)
        self.cant_productos += cant
        self.total += precio * cant
    
        return f"Producto '{producto}' agregado correctamente. Total de productos: {self.cant_productos}"

    def eliminarProducto(self, producto:str, precio:float, cant:int): #string

        self.list_productos.remove(producto)
        self.cant_productos -= cant
        self.total -= precio * cant

        return f"Producto '{producto}' eliminado correctamente. Total de productos: {self.cant_productos}"
    
    def calcularTotal(self): #float
        pass