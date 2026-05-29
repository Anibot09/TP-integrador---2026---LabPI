
def caso_menu_3(almacen,carrito, inventario, proveedor, dep):
    pass
                        
def caso_menu_5(Negocio, carrito):
    prod = input("Ingrese el nombre del producto:")
    carrito.ver_stock_producto(Negocio, prod)

def mostrar_menu(Negocio, carrito, inventario, promociones, almacen, proveedor, dep):
    op = -1
    while op != 0:
        print("\n☆〜-Bienvenido a SuperMarket IoT-〜☆")
        print("1. Ver productos (por góndola).")
        print("2. Ver promociones de la semana.")
        print("3. Agregar producto al carrito.")
        print("4. Eliminar producto del carrito.")
        print("5.Ver stock de un producto.")
        print("6. Ir a pagar y finalizar compra.")
        print("0. Cancelar compra.")
        try:
            op = int(input("Ingrese el numero de la acción que desea realizar: "))
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
                            gond = int(input("\nIngrese el numero de la gondola a la que desea ingresar: "))
                            if gond<0 or gond>=max_gond:
                                raise ValueError
                            
                            gondola_elegida = Negocio[gond]

                            print(f"\nProductos en {gondola_elegida.mi_nom()}:")

                            for producto in gondola_elegida.mis_productos():
                                print(producto)
                            
                            while True:
                                print("\n1. Volver a las góndolas.")
                                print("2. Volver al menú principal.")
                                print("3. Ver stock de un producto.")
                                try:
                                    opcion = int(input("Seleccione una opción: "))

                                    if opcion == 1:
                                        break
                                    elif opcion == 2:
                                        break
                                    elif opcion == 3:
                                        caso_menu_5(Negocio, carrito)
                                        break
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print("Ingrese 1 o 2")
                            
                            if opcion == 2:
                                break

                        except ValueError:
                            print("Debe ingresar un número")              
                case 2:
                    while True:
                        print("\n1. Ver todas las promociones.")
                        print("2.Buscar promoción por producto")
                        print("0.Volver al menú")
                        try: 
                            opcion=int(input("\nIngrese una opción: "))
                            if opcion == 1:
                                carrito.ver_promociones(promociones, Negocio)
                            elif opcion == 2:
                                prod = str(input("\nIngrese el nombre del producto: "))
                                carrito.ver_promociones_producto(promociones, Negocio, prod)
                            elif opcion == 0:
                                break
                            else: 
                                raise ValueError
                        except ValueError:
                            print("Ingrese un numero, por favor.")
                case 3:
                    while True:
                        prod = str(input("\nIngrese el nombre del producto que desea agregar: ")).lower()
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
                        prod = str(input("\nIngrese el nombre del producto que desea eliminar: "))
                        cant = int(input("\nIngrese la cantidad de artículos que dese eliminar: "))
                        almacen.monitorear_eliminacion(prod, cant, carrito, inventario, )
                        while True:
                            try:
                                opcion = int(input(
                                    "\n1. Eliminar otro producto/s\n"
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
                    caso_menu_5(Negocio, carrito)
                case 6:
                    pass
                case 0:
                    print("Su compra fue cancelada. ¡Esperamos que vuelva otro día!")
                    break
        except ValueError:
            print("Ingreso un valor inválido. Por favor, ingrese un número.")
