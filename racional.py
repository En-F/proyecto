import math

class Racional:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numer = num
        self.denom = den
        self.simplificar()

    def numerador(self):
        return self.numer

    def denominador(self):
        return self.denom

    def mult(self, otro):
        n = self.numerador() * otro.numerador()
        d = self.denominador() * otro.denominador()
        return Racional(n, d)
    
    def simplificar(self):
        mcd = math.gcd(self.numer, self.denom)
        self.numer = self.numer // mcd
        self.denom = self.denom // mcd


r = Racional(3, 4)
t = Racional(5, 6)

print(f"Racional 1: {r.numer}/{r.denom}")
print(f"Racional 2: {t.numer}/{t.denom}")
