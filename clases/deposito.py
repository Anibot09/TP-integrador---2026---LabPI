from clases.Productos.producto import Producto



class Deposito():

    
    def __init__(self, cod: int, st: int, nom):
        self.cod = cod
        self.stock = st
        self.nombreDeposito = nom
        self.stock_reserva: dict[Producto, int] = {}


    def agregar_producto(self, producto, st: int):
        if producto in self.stock_reserva:
            self.stock_reserva[producto] += st
        else:
            self.stock_reserva[producto] = st


    def reponer_producto(self, producto, cantidad):#busca el producto en deposito si hay stock repone, sino
        #si existe el producto
        if producto in self.stock_reserva:
            st = self.stock_reserva [producto] #stock del producto en deposito
            #si existe el stock sufi
            if cantidad <= st:
                prods = []
                self.stock_reserva[producto] -= cantidad
                print(f"{cantidad} transferidos desde {self.nombreDeposito}")
                prods.append(producto)
                prods.append(cantidad)
                return prods #devuelve la lista
            #no existe stock sufi
            else:
                return 0
        #no esta el prosucto en el deposito
        else:
            return 0    

#buenas practicas 
    def nombre_deposito (self):
        return self.nombreDeposito
    
    def mi_reserva(self):
        return self.stock_reserva
