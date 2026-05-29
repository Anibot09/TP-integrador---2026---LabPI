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

def main():

    p = Pan(123, "flauta", "nona", 200, 3, 1, 1, 1)
    #Productos tipo(Prod. gral.): Galletitas
    galletita_1 =  Producto_gral(712, "melba", "Terrabusi", 400, 15, 2)
    galletita_2 =  Producto_gral(703, "pepitos", "Mondelez", 320, 76, 2)
    galletita_3 =  Producto_gral(708, "pepas", "Terepin", 245, 23, 2)
    #Productos tipo(Prod. gral.): Perfumes
    perfume_1 =  Producto_gral(712, "melba", "Terrabusi", 400, 15, 2)
    perfume_2 =  Producto_gral(703, "melba", "Terrabusi", 400, 15, 2)
    perfume_3 =  Producto_gral(708, "melba", "Terrabusi", 400, 15, 2)
    #Productos tipo(Prod. gral.): Electrodoméstico
    galletita_1 =  Producto_gral(712, "Melba", "Terrabusi", 400, 15, 2)
    galletita_2 =  Producto_gral(703, "Melba", "Terrabusi", 400, 15, 2)
    galletita_3 =  Producto_gral(708, "Melba", "Terrabusi", 400, 15, 2)
    #Productos tipo(Prod. gral.): Jueguetes
    galletita_1 =  Producto_gral(712, "Melba", "Terrabusi", 400, 15, 2)
    galletita_2 =  Producto_gral(703, "Melba", "Terrabusi", 400, 29, 2)
    galletita_3 =  Producto_gral(708, "Melba", "Terrabusi", 400, 7, 2)
    #Productos tipo(Líquidos): Gaseosas
    bebida_1 =  Liquido(504, "sprite", "Coca-Cola Company", 250, 13, 1, 500)
    bebida_2 =  Liquido(525, "agua con gas", "Villa del Sur", 250, 13, 1, 500)
    bebida_3 =  Liquido(504, "jugo", "Cepita", 250, 13, 1, 500)
    #Productos tipo: Carnes
    carne_1 = Carne(156, "bandeja de matambre", "-", 5000, 7, 2, 15)
    carne_2 = Carne(198, "bandeja de bondiola", "-", 5000, 7, 2, 15)
    carne_3 = Carne(102, "bandeja de vacío", "-", 15000, 7, 1, 15)
    perfume1 = Producto_gral(608, "mandarina", "ooo", 7230, 19, 2)
    perfume2 = Producto_gral(608, "magnolia", "iii", 9000, 2, 2)

    Carnes = Carniceria(100, "Carnicería", [], 0)
    #Panes = Panaderia()
    #Verduras = Verduleria()
    #Bebidas = GondolaGaseosa()
    Perfumeria = Gondola(600, "Perfumeria", [perfume1, perfume2], 2)
    Galletitas = Gondola(700, "Galletas", [galletita_1, galletita_2, galletita_3], 51)
    Electrodomesticos = Gondola(800, "Electrodomesticos", [], 4)
    Juguetes = Gondola(900, "Jugueteria", [], 8)

    Negocio = [Perfumeria, Galletitas, Carnes]

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

    carrito = Carrito()
    
    inventario.ubicarProducto([carne_1, 5])
    for gondola in Negocio:
        for producto in gondola.mis_productos():
            print(producto) 
    """
    
    op = -1
    while op != 0:
        print("\n--Bienvenido su carrito--")
        print("1. Ver productos (por góndola).")
        print("2. Ver promociones de la semana.")
        print("3. Agregar producto al carrito.")
        print("4. Eliminar producto del carrito.")
        print("5. Ir a pagar y finalizar compra.")
        print("0. Cancelar compra.")
        try:
            op = int(input("Ingrese el numero de la acción que desea realizar:"))
            if op<0 or op>5:
                raise ValueError
            match op:
                case 1:
                    while True:
                        max_gond = len(Negocio)
                        print("---Góndolas---")
                        for i in range(max_gond):
                            print(f"{i}. {Negocio[i].mi_nom()}")
                        try:
                            gond = int(input("\nIngrese el la gondola a la que desea ingresar. (Ingrese un numero de opcion): "))
                            if gond<0 or gond>=max_gond:
                                raise ValueError
                            
                            gondola_elegida = Negocio[gond]

                            print(f"\nProductos en {gondola_elegida.mi_nom()}:")

                            for producto in gondola_elegida.mis_productos():
                                print(producto)
                            
                            while True:
                                print("\n1. Volver a las góndolas")
                                print("2. Volver al menú principal")
                                opcion = int(input("Seleccione una opción: "))

                                if opcion == 1:
                                    return False
                                elif opcion == 2:
                                    break
                                else:
                                    raise ValueError

                            if opcion == 2:
                                break

                        except ValueError:
                            print("Debe ingresar un número")              
                case 2:
                    carrito.ver_promociones(promociones, Negocio)
                case 3:
                    while True:
                        prod = str(input("\nIngrese el nombre del producto que desea agregar:")).lower()
                        cant = int(input("\nIngrese la cantidad de artículos que dese adquirir: "))
                        almacen.monitorear_compra(prod, cant, carrito, inventario, proveedor, dep)
                        while True:
                            try:
                                opcion = int(input(
                                    "\n1. Seguir agregando\n"
                                    "2. Volver al menú\n"
                                    "Seleccione una opción: "))

                                if opcion == 1 or opcion == 2:
                                    break
                            
                                print("Ingrese 1 o 2")

                            except ValueError:
                                print("Debe ingresar un número")

                        if opcion == 2:
                            break
                case 4:
                    while True:
                        prod = str(input("\nIngrese el nombre del producto que desea agregar:"))
                        cant = int(input("\nIngrese la cantidad de artículos que dese adquirir: "))
                        almacen.monitorear_eliminacion(prod, cant, carrito, inventario, )
                        while True:
                            try:
                                opcion = int(input(
                                    "\n1. Seguir eliminando productos\n"
                                    "2. Volver al menú\n"
                                    "Seleccione una opción: "))

                                if opcion == 1 or opcion == 2:
                                    break
                            
                                print("Ingrese 1 o 2")

                            except ValueError:
                                print("Debe ingresar un número")

                        if opcion == 2:
                            break
                case 5:
                    pass
                case 0:
                    print("Su compra fue cancelada. ¡Esperamos que vuelva otro día!")
                    break
        except ValueError:
            print("Ingreso un valor inválido. Por favor, ingrese un número.")
"""
if __name__ == "__main__":
    main()
