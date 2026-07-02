#Productos
from clases.Productos.pan import Pan
from clases.Productos.perfume import Perfume
from clases.Productos.galletitas import Galletitas
from clases.Productos.electro import Electro
from clases.Productos.juguete import Juguete
from clases.Productos.liquido import Liquido
from clases.Productos.carne import Carne
from clases.Productos.verdura import Verdura
#Gondolas
from clases.Gondolas.carniceria import Carniceria
from clases.Gondolas.gaseosa import GondolaGaseosa
from clases.Gondolas.perfumeria import Perfumeria
from clases.Gondolas.galletita import GondolaGalletitas
from clases.Gondolas.electrodomesticos import Electrodomestiscos
from clases.Gondolas.juguete import Jugueteria
from clases.Gondolas.panaderia import Panaderia
from clases.Gondolas.verduleria import Verduleria

from clases.promociones import Promociones
from clases.deposito import Deposito



#Productos tipo(ex p gral): Galletitas
galletita_1 =  Galletitas(712, "melba", "terrabusi", 400, 15, 2, "galletita")
galletita_2 =  Galletitas(703, "pepitos", "mondelez", 320, 76, 2, "galletita")
galletita_3 =  Galletitas(708, "pepas", "terepin", 245, 23, 2, "galletita")
#Productos tipo(ex p gral): Perfumes
perfume_1 =  Perfume(622, "crema", "avon", 3500, 15, 3, 150, "perfumeria")
perfume_2 =  Perfume(634, "suavizante lavanda", "vivere", 6300, 11, 2, 500, "perfumeria")
perfume_3 =  Perfume(678, "jabon liquido", "dove", 8900, 23, 2, 250, "perfumeria")
#Productos tipo(ex p gral): Electrodoméstico
electro_1 =  Electro(823, "microondas", "phillips", 45000, 5, 1, 12, "electro")
electro_2 =  Electro(884, "licuadora", "oster", 24000, 18, 1, 12, "electro")
electro_3 =  Electro(811, "tostadora", "atma", 15000, 23, 1, 6, "electro")
#Productos tipo(ex p gral.): Juguetes
juguete_1 =  Juguete(931, "auto control remoto", "hot wheels", 9000, 15, 2, "juguete")
juguete_2 =  Juguete(983, "monopoly", "hasbro", 16700, 29, 2, "juguete")
juguete_3 =  Juguete(901, "osito de peluche", "ty", 14000, 7, 2, "juguete")
#Productos tipo(Líquidos): Gaseosas
bebida_1 =  Liquido(504, "sprite", "coca-cola Company", 250, 13, 1, 500, "bebida")
bebida_2 =  Liquido(525, "agua con gas", "villavicencio", 250, 13, 1, 500, "bebida")
bebida_3 =  Liquido(513, "jugo de naranja", "citric", 250, 13, 1, 500, "bebida")
bebida_4 =  Liquido(510, "coca cola", "Coca-Cola Company", 300, 17, 1, 250, "bebida")
#Productos tipo: Carnes
carne_1 = Carne(156, "bandeja de matambre", "vacas muertas", 5000, 7, 2, 3, "carne")
carne_2 = Carne(198, "bandeja de bondiola", "vacas muertas", 5000, 13, 2, 4, "carne")
carne_3 = Carne(102, "bandeja de vacio", "vacas muertas", 15000, 17, 1, 2, "carne")
#Productos tipo: Panes 
pan_1 = Pan(210, "pan francés", "la Espiga", 800, 20, 5, 0.5, 10, "pan")
pan_2 = Pan(211, "pan de molde", "bimbo", 1200, 15, 3, 0.8, 5, "pan")
pan_3 = Pan(212, "pan negro", "la Nona", 1500, 30, 10, 0.3, 12, "pan")
#Productos tipo: Verduras
verdura_1 = Verdura(310, "tomate", "Campo Verde", 500, 20, 5, 1, "verdura")
verdura_2 = Verdura(311, "lechuga", "Campo Verde", 300, 15, 3, 1, "verdura")
    
    
Carnes = Carniceria(100, "Carniceria", [carne_1, carne_2, carne_3], 37)
Panes = Panaderia(200, "Panaderia", [pan_1, pan_2, pan_3], 65)
Verduras = Verduleria(300, "Verduleria", [verdura_1, verdura_2], 35)
Bebidas = GondolaGaseosa(400, "Bebidas", [bebida_1, bebida_2, bebida_3, bebida_4], 56)
Perfumes = Perfumeria(600, "Perfumeria", [perfume_1, perfume_2, perfume_3], 49)
Galles = GondolaGalletitas(700, "Galletas", [galletita_1, galletita_2, galletita_3], 51)
Electros = Electrodomestiscos(800, "Electrodomesticos", [electro_1, electro_2, electro_3], 46)
Juguetes = Jugueteria(900, "Jugueteria", [juguete_1, juguete_2, juguete_3], 51)

Negocio = [Carnes, Panes, Verduras, Bebidas, Perfumes, Galles, Electros, Juguetes]

# promos = {703:{"producto": "pepitos", "marca":"Mondelez", "promo":"2x1"},
#            712:{"producto": "melba", "marca":"Terrabusi", "promo":"2x1"},
#            708:{"producto": "pepas", "marca":"Terepín", "promo":"2x1"},
#            504:{"producto": "sprite", "marca":"Coca-Cola Company", "promo":"30 descuento(2da/misma marca)"},
#            525:{"producto": "agua con gas", "marca":"Villa del Sur", "promo":"30 descuento(2da/misma marca)"},
#            513:{"producto": "jugo", "marca":"Cepita", "promo":"30 descuento(2da/misma marca)"},
#            510:{"producto":"coca-cola", "marca":"Coca-Cola Company", "promo":"30 descuento(2da/misma marca)"},
#            622:{"producto": "Perfume Floral", "marca":"Avon", "promo":"50 descuento"},
#            634:{"producto": "suavizante lavanda", "marca":"Vivere", "promo":"50 descuento"},
#            678:{"producto": "jabon liquido", "marca":"Dove", "promo":"50 descuento"}

promociones = Promociones()

#Llenando promos

promociones.agregar_promo("703", "pepitos", "mondelez", "2X1")   
promociones.agregar_promo("712", "melba", "terrabusi", "2x1")
promociones.agregar_promo("708", "pepas", "terepin", "2x1")
promociones.agregar_promo("504", "sprite", "coca-cola company", "30 OFF (2da/misma marca)")
promociones.agregar_promo("525", "agua con gas", "villavicencio", "30 OFF (2da/misma marca)")
promociones.agregar_promo("513", "jugo de naranja", "citric", "30 OFF (2da/misma marca)")
promociones.agregar_promo("510", "coca cola", "coca-cola company", "30 OFF (2da/misma marca)")
promociones.agregar_promo("622", "crema", "avon", "50 OFF")   
promociones.agregar_promo("674", "suavizante lavanda", "vivere", "50 OFF")   
promociones.agregar_promo("678", "jabon liquido", "dove", "50 OFF") 

dep = Deposito(234, 45, "Depot")

#Llenando depósito
dep.agregar_producto(carne_1, 5)
dep.agregar_producto(galletita_1, 7)
dep.agregar_producto(carne_2, 30)
dep.agregar_producto(galletita_2, 17)
dep.agregar_producto(carne_3, 26)
dep.agregar_producto(galletita_3, 32)
dep.agregar_producto(pan_1, 15)
dep.agregar_producto(pan_2, 50)
dep.agregar_producto(pan_3, 1)
dep.agregar_producto(bebida_1, 34)
dep.agregar_producto(bebida_2, 46)
dep.agregar_producto(bebida_3, 12)
dep.agregar_producto(verdura_1, 53)
dep.agregar_producto(verdura_2, 27)
dep.agregar_producto(perfume_1, 5)
dep.agregar_producto(perfume_2, 12)
dep.agregar_producto(perfume_3, 25)
dep.agregar_producto(electro_1, 16)
dep.agregar_producto(electro_2, 7)
dep.agregar_producto(electro_3, 9)
dep.agregar_producto(juguete_1, 19)
dep.agregar_producto(juguete_2, 13)
dep.agregar_producto(juguete_3, 23)

