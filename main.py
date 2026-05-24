"""TP Integrador - Lab. PI"""
from clases.almacen import Almacen
from clases.deposito import Deposito
from clases.Productos.pan import Pan
from clases.promociones import Promociones
p = Pan(123, "flauta", "nona", 200, 3, 1, 1, 1)  
#este funca
print(p)
"""promos = {703:{"producto": "Pepitos", "marca":"Mondelez", "promo":"2x1"},
          712:{"producto": "Melba", "marca":"Terrabusi", "promo":"2x1"},
          708:{"producto": "Pepas", "marca":"Terepín", "promo":"2x1"}, 
          504:{"producto": "Sprite", "marca":"Coca-Cola Company", "promo":"30 descuento(2da/misma marca)"},
          525:{"producto": "Agua con gas", "marca":"Villa del Sur", "promo":"30 descuento(2da/misma marca)"},
          513:{"producto": "Jugo", "marca":"Cepita", "promo":"30 descuento(2da/misma marca)"},
          612:{"producto": "lavanda", "marca":"aaa", "promo":"50 descuento"},
          605:{"producto": "jazmín", "marca":"eee", "promo":"50 descuento"},
          608:{"producto": "magnolia", "marca":"iii", "promo":"50 descuento"}}

promociones = Promociones(promos)

print(promociones.mis_productos_promos())"""

#dep = Deposito(234, 45, "Depot")

#dep.agregar_producto(p, 12)