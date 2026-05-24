from clases.Productos.producto import Producto

class Deposito():
    def __init__(self, cod: int, st: int, nombreDeposito: str):
        self.nombreDeposito = "sotano"
        self.cod = cod
        self.stock = st
        self.stock_reserva: dict[Producto, int] = {}

    def agregar_producto(self, producto, st: int):
        #st = self.stock_reserva [producto] /esta linea generaba error porque inmediatamente perdes el valor st que te pasaron
        if producto in self.stock_reserva:
            self.stock_reserva[producto] += st
        else:
            self.stock_reserva[producto] = st

    def reponer_producto(self, producto, cantidad, st: int):#busca el producto en deposito si hay stock repone, sino
        st = self.stock_reserva [producto] #stock del producto en deposito
        if producto in self.stock_reserva and cantidad <= st:
            prods = []
            st -= cantidad
            self.stock_reserva[producto.mi_stock] -= cantidad
            print(f"{cantidad} transferidos desde {self.nombreDeposito}")
            prods.append(producto.mi_codigo())
            prods.append(cantidad)
            return prods 
        else: 
            if self.stock_reserva[producto] == 0:
                return 0
        return f"Quedan {self.stock_reserva[producto]} {self.stock_reserva[producto.mi_nombre()]} /n codigo: {self.stock_reserva[producto.mi_codigo()]}"
    

    def nombre_deposito (self):
        return self.nombreDeposito
    
    def mi_reserva(self):
        return self.stock_reserva
