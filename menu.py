def caso_menu_agregar(almacen, carrito,inventario, proveedor,dep):
    while True:
        prod = str(input("\nIngrese el nombre del producto que desea agregar: ")).lower()
        cant = int(input("\nIngrese la cantidad de artículos que dese adquirir: "))
        resultado = almacen.monitorear_compra(prod, cant, carrito, inventario, proveedor, dep)
        if resultado:
            print("Producto agregado correctamente.")
        else:
            print("No se pudo agregar el producto.")
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
            
def caso_menu_ver_stock(catalogo, carrito):
    prod = input("Ingrese el nombre del producto:")
    carrito.ver_stock_producto(catalogo, prod)

def mostrar_menu(catalogo, carrito, inventario, promociones, almacen, proveedor, dep):
    op = -1
    while op != 0:
        print("\n☆〜-Bienvenido a SuperMarket IoT-〜☆")
        print("1. Ver productos (por góndola).")
        print("2. Ver promociones de la semana.")
        print("3. Agregar producto al carrito.")
        print("4. Eliminar producto del carrito.")
        print("5. Ver stock de un producto.")
        print("6. Ver su carrito.")
        print("7. Ir a pagar y finalizar compra.")
        print("0. Cancelar compra.")
        try:
            op = int(input("Ingrese el numero de la acción que desea realizar: "))
            if op<0 or op>7:
                raise ValueError
            match op:
                case 1:
                    while True:
                        max_gond = len(catalogo)
                        print("---Góndolas---")
                        for i in range(max_gond):
                            print(f"{i+1}. {catalogo[i].mi_nom()}")
                        try:
                            gond = int(input("\nIngrese el numero de la gondola a la que desea ingresar o ingrese 0 para volver al menu: "))
                            if gond<0 or gond>max_gond:
                                raise ValueError
                            elif gond == 0:
                                break 

                            gondola_elegida = catalogo[gond-1]

                            print(f"\nProductos en {gondola_elegida.mi_nom()}:")

                            for producto in gondola_elegida.mis_productos():
                                print(producto)
                            
                            while True:
                                print("\n1. Agregar producto al carrito.")
                                print("2. Ver stock de un producto.")
                                print("3. Volver a las góndolas.")
                                print("4. Volver al menú principal.")
                               
                                try:
                                    opcion = int(input("Seleccione una opción: "))

                                    if opcion == 1:
                                        caso_menu_agregar(almacen, carrito,inventario, proveedor,dep)
                                    elif opcion == 2:
                                        caso_menu_ver_stock(catalogo, carrito)
                                        break
                                    elif opcion == 3:
                                        break
                                    elif opcion == 4:
                                        break
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print("Ingrese un numero del 1 al 4")

                        except ValueError:
                            print("Debe ingresar un número")              
                case 2:
                    while True:
                        print("\n1. Ver todas las promociones.")
                        print("2. Buscar promoción por producto")
                        print("3. Agregar producto al carrito.")
                        print("0. Volver al menú")
                        try: 
                            opcion=int(input("\nIngrese una opción: "))
                            if opcion == 1:
                                carrito.ver_promociones(promociones, catalogo)
                            elif opcion == 2:
                                prod = str(input("\nIngrese el nombre del producto: "))
                                carrito.ver_promociones_producto(promociones, catalogo, prod)
                            elif opcion == 3:
                                caso_menu_agregar(almacen, carrito, inventario, proveedor, dep)
                            elif opcion == 0:
                                break
                            else: 
                                raise ValueError
                        except ValueError:
                            print("Ingrese un numero, por favor.")
                case 3:
                    caso_menu_agregar(almacen, carrito,inventario, proveedor,dep)
                    break
                case 4:
                    while True:
                        prod = str(input("\nIngrese el nombre del producto que desea eliminar: "))
                        cant = int(input("\nIngrese la cantidad de artículos que dese eliminar: "))
                        almacen.monitorear_eliminacion(prod, cant, carrito)
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
                    caso_menu_ver_stock(catalogo, carrito)
                case 6:
                    print("\n--- Mi Carrito ---")
                    if carrito.mis_productos() == []:
                        print("Su carrito se encuentra vacio! Agregue articulos para visualizarlos.")
                    else:
                        for producto, cantidad in carrito.mis_productos():
                            print(f"{producto} | Cantidad: {cantidad}")
                        print(f"Su total es: {carrito.mi_total()}")
                case 7:
                    print("\n--- Carrito final ---")
                    for prod in carrito.mis_productos():
                        print(prod)
                    print(f"Total a pagar: {carrito.total}")
                    print("¡Gracias por su compra!Hasta la próxima :)")
                    op = 0
                case 0:
                    print("Su compra fue cancelada. ¡Esperamos que vuelva otro día!")
                    break
        except ValueError:
            print("Ingreso un valor inválido. Por favor, ingrese un número.")
