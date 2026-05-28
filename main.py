"""TP Integrador - Lab. PI"""
from clases.almacen import Almacen
from clases.deposito import Deposito
from clases.Productos.pan import Pan
from clases.Productos.producto_gral import Producto_gral
from clases.Productos.liquido import Liquido
from clases.Productos.carne import Carne
from clases.promociones import Promociones
from clases.carrito import Carrito
from clases.Gondolas.gondola import Gondola
from clases.inventario import Inventario

p = Pan(123, "flauta", "nona", 200, 3, 1, 1, 1)
#Productos tipo(Prod. gral.): Galletitas
galletita_1 =  Producto_gral(712, "Melba", "Terrabusi", 400, 15, 2)
galletita_2 =  Producto_gral(703, "Melba", "Terrabusi", 400, 15, 2)
galletita_3 =  Producto_gral(708, "Melba", "Terrabusi", 400, 15, 2)
#Productos tipo(Líquidos): Gaseosas
bebida_1 =  Liquido(504, "Sprite", "Coca-Cola Company", 250, 13, 1, 500)
bebida_2 =  Liquido(525, "Agua con gas", "Villa del Sur", 250, 13, 1, 500)
bebida_3 =  Liquido(504, "Jugo", "Cepita", 250, 13, 1, 500)
#Productos tipo: Carnes
carne_1 = Carne(156, "Bandeja de Matambre", "-", 5000, 7, 2, 15)
carne_2 = Carne(156, "Bandeja de Bondiola", "-", 5000, 7, 2, 15)
carne_3 = Carne(156, "Bandeja de Vacío", "-", 15000, 7, 1, 15)
perfume1 = Producto_gral(608, "mandarina", "ooo", 7230, 19, 2)
perfume2 = Producto_gral(608, "magnolia", "iii", 9000, 2, 2)

#este funca
#print(p)
"""
perfumeria = Gondola(600, "Perfumeria", [perfume1, perfume2], 2)
galletitas = Gondola(400, "Galletas", [galle], 1)

Negocio = [perfumeria, galletitas]

promos = {703:{"producto": "Pepitos", "marca":"Mondelez", "promo":"2x1"},
          712:{"producto": "Melba", "marca":"Terrabusi", "promo":"2x1"},
          708:{"producto": "Pepas", "marca":"Terepín", "promo":"2x1"}, 
          504:{"producto": "Sprite", "marca":"Coca-Cola Company", "promo":"30 descuento(2da/misma marca)"},
          525:{"producto": "Agua con gas", "marca":"Villa del Sur", "promo":"30 descuento(2da/misma marca)"},
          513:{"producto": "Jugo", "marca":"Cepita", "promo":"30 descuento(2da/misma marca)"},
          612:{"producto": "lavanda", "marca":"aaa", "promo":"50 descuento"},
          605:{"producto": "jazmín", "marca":"eee", "promo":"50 descuento"},
          608:{"producto": "magnolia", "marca":"iii", "promo":"50 descuento"}}

promociones = Promociones(promos)

almacen = Almacen(654, promociones, Negocio)

#prec = almacen.calcular_promociones(perfume, 3)
#print(prec)


dep = Deposito(234, 45, "Depot")

dep.agregar_producto(p, 15)
#print(dep.mi_reserva())
#print(dep.reponer_producto(p,3))
inventario = Inventario(7654, dep, Negocio)

carrito = Carrito()
#carrito.agregarProducto("magnolia", 3, almacen)
#carrito.agregarProducto("Melba", 3, almacen)
#carrito.eliminarProducto("magnolia", 1, almacen)

almacen.monitorear_compra("magnolia", 3, carrito, inventario)
"""