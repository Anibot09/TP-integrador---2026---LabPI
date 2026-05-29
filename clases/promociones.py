from clases.Productos.producto import Producto

class Promociones:
    def __init__(self, prod_pomos: dict):
        self.productos_promos = prod_pomos

            
    def mis_productos_promos(self): #devuelve que productos tienen promociones
        resultado = []

        for codigo, datos in self.productos_promos.items():
            resultado.append((codigo, datos["producto"], datos["marca"]))

        return resultado

    def mis_promos(self):
        return self.productos_promos
    
#    def agregar_promocion(self, codigo, promo):
#        self.productos_promos[codigo] = {
#            "producto" : Producto.mi_nombre,
#            "marca" : Producto.mi_marca,
#            "promo": promo
#        } 