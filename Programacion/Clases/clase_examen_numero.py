"""
Numeros
"""
from abc import ABC , abstractmethod

class Expresiones(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def valor(self):
        """Devuelve el valor de la expresion"""

class Suma(Expresiones):
    """Realiza la operacion de dos numeros"""

    def __init__(self,x , y):
        self.__set_x(x)
        self.__set_y(y)

    def __set_x(self, x):
        self.__x = x

    def get__x(self):
        return self.__x
    
    def __set_y(self, y):
        self.__y = y

    def get__y(self):
        return self.__y

    def valor(self):
        return self.get__x().valor() + self.get__y().valor()  

class Numero(Expresiones):
    """Creo un numero"""
    
    def __init__(self,x):
        self.__set_numero(x)
  
    def __set_numero(self, x):
        self.__x = x

    def valor(self):
        return self.__x
    
        

class Producto(Expresiones):
    """Realizas el Producto de dos numeros"""
    def __init__(self, x, y ):
        self.__set_x(x)
        self.__set_y(y)

    def __set_x(self, x):
        if x.valor() > 0:
            self.__x = x
        else:
            raise ValueError ("Eres un pringao")

    def get__x(self):
        return self.__x
    
    def __set_y(self, y):
        self.__y = y

    def get__y(self):
        return self.__y

    def valor(self):
        return self.get__x().valor() * self.get__y().valor()

print(Numero(2).valor())
print(Suma(Numero(2), Producto(Numero(1), Numero(5))).valor())
print(Producto(Numero(2), Suma(Numero(3), Numero(5))).valor())