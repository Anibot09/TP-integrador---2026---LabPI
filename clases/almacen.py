from clases.Productos.carne import Carne
from clases.Productos.pan import Pan
from clases.Productos.verdura import Verdura
from clases.Productos.liquido import Liquido
from clases.promociones import Promociones

class Almacen():
    def __init__(self, num, promos: Promociones):
        self.num_id = num
        self.promociones = promos
       
    def determinar_precio(self, producto, cant):#Toma en cuenta cantidades y peso para determinar precios de ciertos productos. 
        if type(producto)== Carne: #Carnes
            precio = producto.mi_precio()
            peso = producto.mi_peso()
            precio_final = (peso*precio)*cant
            return precio_final
        elif type(producto)== Pan:#Panes
            precio = producto.mi_precio()
            bol = producto.mis_bolsones()
            precio_final = (precio*bol)*cant
            return precio_final
        elif type(producto)== Verdura:#Verduras
            precio = producto.mi_precio()
            peso = producto.mi_peso()
            precio_final = (peso*precio)*cant
            return precio_final
        #elif type(producto)== Liquido:#Bebidas
        #    precio = producto.mi_precio()
        #    litros = producto.mi_litro()
        #    precio_final = (litros*precio)*cant
        #    return precio_final
        else:
            precio = producto.mi_precio()
            precio_final = precio*cant
            return precio_final
        
            
    def calcular_promociones(self, producto, cant):
        promociones = self.promociones.mis_promos()
        if producto.mi_codigo() in promociones:
            precio = producto.mi_precio()
            promo = promociones[producto.mi_codigo()] 
            if promo['promo'] == "2x1":
                if cant>=2:
                    if cant % 2 == 0:
                        precio_final = (cant/2)*precio 
                    else:
                        precio_final = ((cant//2)+1)*precio #división de enteros //
                    return precio_final
                else:
                    print("No hay cantidad necesaria para agregar el descuento.")
                    return precio
            elif promo["promo"] == "30 descuento(2da/misma marca)":
                if cant>=2:
                    if cant % 2 == 0:
                        precio_final = (cant/2)*(precio + (precio-(precio*0.30)))
                    else:
                        sobrantes = cant % 2
                        precio_final = (cant//2)*(precio + (precio-(precio*0.30))) + sobrantes*precio
                    return precio_final
                else:
                    print("No hay cantidad necesaria para agregar el descuento.")
                    return precio
            elif promo["promo"] == "50 descuento":
                precio_final = cant*(precio - precio*0.50)
                return precio_final
        else:
            #print("Producto sin promoción")
            return 0
    
    def monitorear_compra(): #chequea que el estado de los productos y gondolas al  realizar la compra
        pass
    
    def actualizar_stock():
        pass
    