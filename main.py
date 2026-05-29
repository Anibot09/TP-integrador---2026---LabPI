"""TP Integrador - Lab. PI"""
from clases.almacen import Almacen
from clases.deposito import Deposito
#Productos
from clases.Productos.pan import Pan
from clases.Productos.producto_gral import Producto_gral
from clases.Productos.liquido import Liquido
from clases.Productos.carne import Carne
from clases.Productos.verdura import Verdura
#Gondolas
from clases.Gondolas.carniceria import Carniceria
from clases.Gondolas.gaseosas import GondolaGaseosa
from clases.Gondolas.gondola import Gondola
from clases.Gondolas.panaderia import Panaderia
from clases.Gondolas.verduleria import Verduleria

from clases.promociones import Promociones
from clases.proveedor import Proveedor
from clases.carrito import Carrito
from clases.inventario import Inventario
import menu

def main():

    p = Pan(123, "flauta", "nona", 200, 3, 1, 1, 1)
    #Productos tipo(Prod. gral.): Galletitas
    galletita_1 =  Producto_gral(712, "melba", "Terrabusi", 400, 15, 2)
    galletita_2 =  Producto_gral(703, "pepitos", "Mondelez", 320, 76, 2)
    galletita_3 =  Producto_gral(708, "pepas", "Terepin", 245, 23, 2)
    #Productos tipo(Prod. gral.): Perfumes
    perfume_1 =  Producto_gral(712, "", "", 400, 15, 2)
    perfume_2 =  Producto_gral(703, "", "", 400, 15, 2)
    perfume_3 =  Producto_gral(708, "", "", 400, 15, 2)
    #Productos tipo(Prod. gral.): Electrodoméstico
    electro_1 =  Producto_gral(712, "microondas", "Phillips", 3000, 5, 1)
    electro_2 =  Producto_gral(703, "licuadora", "Terrabusi", 24000, 18, 1)
    electro_3 =  Producto_gral(708, "tostadora", "Terrabusi", 15000, 23, 1)
    #Productos tipo(Prod. gral.): Jueguetes
    juguete_1 =  Producto_gral(712, "", "", 400, 15, 2)
    juguete_2 =  Producto_gral(703, "", "", 400, 29, 2)
    juguete_3 =  Producto_gral(708, "", "", 400, 7, 2)
    #Productos tipo(Líquidos): Gaseosas
    bebida_1 =  Liquido(504, "sprite", "Coca-Cola Company", 250, 13, 1, 500)
    bebida_2 =  Liquido(525, "agua con gas", "Villa del Sur", 250, 13, 1, 500)
    bebida_3 =  Liquido(509, "jugo", "Cepita", 250, 13, 1, 500)
    bebida_3 =  Liquido(506, "coca-cola", "Coca-Cola Company", 300, 17, 1, 250)
    #Productos tipo: Carnes
    carne_1 = Carne(156, "bandeja de matambre", "-", 5000, 7, 2, 15)
    carne_2 = Carne(198, "bandeja de bondiola", "-", 5000, 7, 2, 15)
    carne_3 = Carne(102, "bandeja de vacío", "-", 15000, 7, 1, 15)
    perfume1 = Producto_gral(608, "mandarina", "ooo", 7230, 19, 2)
    perfume2 = Producto_gral(608, "magnolia", "iii", 9000, 2, 2)

    Carnes = Carniceria(100, "Carniceria", [], 0)
    #Panes = Panaderia(200, "Panaderia", [], 0)
    #Verduras = Verduleria(300, "Verduleria", [], 0)
    Bebidas = GondolaGaseosa(400, "Bebidas", [bebida_1, bebida_2, bebida_3], 0)
    Perfumeria = Gondola(600, "Perfumeria", [perfume1, perfume2], 2)
    Galletitas = Gondola(700, "Galletas", [galletita_1, galletita_2, galletita_3], 51)
    Electrodomesticos = Gondola(800, "Electrodomesticos", [], 4)
    Juguetes = Gondola(900, "Jugueteria", [], 8)

    Negocio = [Perfumeria, Galletitas, Carnes, Bebidas]

    promos = {703:{"producto": "pepitos", "marca":"Mondelez", "promo":"2x1"},
            712:{"producto": "melba", "marca":"Terrabusi", "promo":"2x1"},
            708:{"producto": "pepas", "marca":"Terepín", "promo":"2x1"},
            504:{"producto": "sprite", "marca":"Coca-Cola Company", "promo":"30 descuento(2da/misma marca)"},
            525:{"producto": "agua con gas", "marca":"Villa del Sur", "promo":"30 descuento(2da/misma marca)"},
            513:{"producto": "jugo", "marca":"Cepita", "promo":"30 descuento(2da/misma marca)"},
            612:{"producto": "lavanda", "marca":"aaa", "promo":"50 descuento"},
            605:{"producto": "jazmín", "marca":"eee", "promo":"50 descuento"},
            608:{"producto": "magnolia", "marca":"iii", "promo":"50 descuento"}}

    promociones = Promociones(promos)

    almacen = Almacen(654, promociones, Negocio)

    dep = Deposito(234, 45, "Depot")
    proveedor = Proveedor("Productos por mayoR S.R.L.", "+54 9 11 3456-0987/prod_mayor455@gmail.com")
    inventario = Inventario(7654, dep, Negocio)

    dep.agregar_producto(carne_1, 5)
    dep.agregar_producto(galletita_1, 7)
    carrito = Carrito()
    
    menu.mostrar_menu(Negocio, carrito, inventario, promociones, almacen, proveedor, dep)    
    
if __name__ == "__main__":
    main()
