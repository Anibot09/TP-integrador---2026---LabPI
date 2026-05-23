from clases.Productos.producto import Producto

class Promociones:
    def __init__(self, prod_pomos: dict):
        self.productos_promos = prod_pomos


    def mostrar_promociones(self):
        for datos in self.productos_promos.items():
            print(f"{datos['producto']} tiene promo {datos['promo']} en marca {datos['marca']}")
            
    def mis_productos_promos(self): #devuelve que productos tienen promociones
        resultado = []

        for codigo, datos in self.productos_promos.items():
            resultado.append((codigo, datos["producto"], datos["marca"]))

        return resultado

#    def agregar_promocion(self, codigo, promo):
#        self.productos_promos[codigo] = {
#            "producto" : Producto.mi_nombre,
#            "marca" : Producto.mi_marca,
#            "promo": promo
#        } 