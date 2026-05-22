from clases.Productos.carne import Carne
from clases.Productos.pan import Pan
from clases.Productos.verdura import Verdura

class Almacen():
    def __init__(self, num, prod, promos):
        self.num_id = num
        self.producto = prod
        self.promociones = promos
       
    def determinar_precio(self):#Toma en cuenta cantidades y peso para determinar precios de ciertos productos. 
        if type(self.producto)== Carne: #Carnes
            peso = self.producto.mi_precio()
            bol = self.producto.mi_peso()
            precio_final = peso*bol
            return precio_final
        elif type(self.producto)== Pan:#Panes
            peso = self.producto.mi_precio()
            bol = self.producto.mis_bolsones()
            precio_final = peso*bol
            return precio_final
        elif type(self.producto)== Verdura:#Verduras
            peso = self.producto.mi_precio()
            bol = self.producto.mi_peso()
            precio_final = peso*bol
            return precio_final
            
    def calcular_promociones(self):
        pass
    
    def monitorear_compra(): #chequea que el estado de los productos y gondolas al  realizar la compra
        pass
    
    def actualizar_stock():
        pass
    