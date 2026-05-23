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

    def reponer_producto(self, producto, cantidad, st: int):
        st = self.stock_reserva [producto] 
        if producto in self.stock_reserva and cantidad >= st:
            self.stock_reserva[producto] -= cantidad
            return f"{cantidad} transferidos desde {self.nombreDeposito}"
        else: 
            if self.stock_reserva[producto] == 0:
                return f"Quedan 0 {self.stock_reserva[producto.nom]} /n codigo: {self.stock_reserva[producto.cod]}"
            return f"Quedan {self.stock_reserva[producto]} {self.stock_reserva[producto.nom]} /n codigo: {self.stock_reserva[producto.cod]}"
    

    def nombre_deposito (self):
        return self.nombreDeposito
    
    def mi_reserva(self):
        return self.stock_reserva
