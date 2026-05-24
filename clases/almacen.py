from clases.Productos.carne import Carne
from clases.Productos.pan import Pan
from clases.Productos.verdura import Verdura

class Almacen():
    def __init__(self, num, promos):
        self.num_id = num
        self.promociones = promos
       
    def determinar_precio(self, producto):#Toma en cuenta cantidades y peso para determinar precios de ciertos productos. 
        if type(producto)== Carne: #Carnes
            peso = producto.mi_precio()
            bol = producto.mi_peso()
            precio_final = peso*bol
            return precio_final
        elif type(producto)== Pan:#Panes
            peso = producto.mi_precio()
            bol = producto.mis_bolsones()
            precio_final = peso*bol
            return precio_final
        elif type(producto)== Verdura:#Verduras
            peso = producto.mi_precio()
            bol = producto.mi_peso()
            precio_final = peso*bol
            return precio_final
            
    def calcular_promociones(self, producto):
        if producto.mi_codigo() in self.promociones:
            if self.promociones["promo"] == "2x1":
                pass
        else:
            #print("Producto sin promoción")
            return 0
    
    def monitorear_compra(): #chequea que el estado de los productos y gondolas al  realizar la compra
        pass
    
    def actualizar_stock():
        pass
    