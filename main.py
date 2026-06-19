"""TP Integrador - Lab. PI"""

from clases.almacen import Almacen
from clases.deposito import Deposito
#Productos
from clases.Productos.pan import Pan
from clases.Productos.electro import Electro
from clases.Productos.perfume import Perfume
from clases.Productos.galletitas import Galletitas
from clases.Productos.juguete import Juguete
from clases.Productos.liquido import Liquido
from clases.Productos.carne import Carne
from clases.Productos.verdura import Verdura
#Gondolas
from clases.Gondolas.carniceria import Carniceria
from clases.Gondolas.gaseosas import GondolaGaseosa
from clases.Gondolas.gondola import Gondola
from clases.Gondolas.panaderia import Panaderia
from clases.Gondolas.verduleria import Verduleria
from clases.Gondolas.electro import Electro
from clases.Gondolas.galletita import Galletita
from clases.Gondolas.perfume import Perfume
from clases.Gondolas.juguete import Juguete

from clases.promociones import Promociones
from clases.proveedor import Proveedor
from clases.carrito import Carrito
from clases.inventario import Inventario
import menu
from catalogo import Negocio, promociones, dep

def main():

    almacen = Almacen(654, promociones, Negocio)

    proveedor = Proveedor("Productos por mayoR S.R.L.", "+54 9 11 3456-0987/prod_mayor455@gmail.com")
    inventario = Inventario(7654, dep, Negocio)
    
    carrito = Carrito()
    
    menu.mostrar_menu(Negocio, carrito, inventario, promociones, almacen, proveedor, dep)    
    
if __name__ == "__main__":
    main()
