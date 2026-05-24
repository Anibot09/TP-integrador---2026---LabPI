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
        
    @abstractmethod
    def mi_precio(self)-> float:
        return self.precio

    @abstractmethod
    def mi_codigo(self)-> float:
        return self.codigoBarra
    
    @abstractmethod
    def mi_nombre(self)-> str:
        return self.nombre
    
    @abstractmethod
    def mi_marca(self)-> str:
        return self.marca
    
    @abstractmethod
    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio}"