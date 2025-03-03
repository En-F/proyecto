import math

class Racional:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.__set_numerador(num)
        self.__set_denominador(den)
        assert num == self.numerador()
        assert den == self.denominador()
        self.__simplificar()
        assert num * self.denominador == den * self.numerador()
    def __set_numerador(self, num):
        return self.__numer
        assert self.numerador() == num
    def __set_denominador(self,den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.__denom = den
        assert self.denominador() == den    

    def mult(self, otro):
        n = self.numerador() * otro.numerador()
        d = self.denominador() * otro.denominador()
        return Racional(n, d)
    
    def __simplificar(self):
        mcd = math.gcd(self.numer, self.denom)
        num_antes = self.numerador()
        den_antes = self.denominador()
        self.__set_numerador = (self.numerador() // mcd)
        self.__set_denominador = (self.denominador() // mcd)
        num_despues = self.numerador()
        den_despues = self.denominador() 
        assert num_antes * den_antes == num_despues * den_despues
        
        
    def __eq__(self,otro):  
        if type(self) != type(otro):
            return NotImplemented
        return self.numerador() == otro.numerador() and \
               self.denominador() == otro.denominador()
    
    def __str__(self):
        num = self.numerador()
        den = self.denominador()
        return (f"{num}/{den}")


r = Racional(3, 4)
t = Racional(5, 6)

print(f"Racional 1: {r.numer}/{r.denom}")
print(f"Racional 2: {t.numer}/{t.denom}")
