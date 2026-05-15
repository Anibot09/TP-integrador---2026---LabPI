from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, cod, nom, marca, price, st, st_min):
        self.codigoBarra = cod
        self.nombre = nom
        self.marca = marca
        self.precio = price
        self.stock = st
        self.stock_min = st_min
        if type (self) is Producto:
            raise TypeError("No se puede instanciar la clase Producto")

