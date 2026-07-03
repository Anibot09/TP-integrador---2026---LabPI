from clases.Productos.producto import Producto



class Promociones:

    
    def __init__(self):
        self.productos_promos = {}

    def agregar_promo(self, codigo, producto, marca, tipo):
        self.productos_promos[codigo] = {
            "producto": producto,
            "marca": marca,
            "promo": tipo
        }   
        
    def mis_productos_promos(self): #devuelve que productos tienen promociones
        resultado = []

        for codigo, datos in self.productos_promos.items():
         resultado.append((codigo, datos["producto"], datos["marca"]))

        return resultado

    def mis_promos(self):
        return self.productos_promos