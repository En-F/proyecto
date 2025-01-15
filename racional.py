class Racional:
    def __init__(self, num, den):
        self.numer = num  # Numerador
        self.denom = den  # Denominador
    
    def numerador(self):
        return self.numer
    
    def denominador(self):
        return self.denom
    
    def mult(self, otro):
        n =  self.numerador() * otro.numerador()
        d =  self.denominador() * otro.denominador()
        return Racional(n, d)

# Crear objetos de la clase Racional
r = Racional(3, 4)
t = Racional(5, 6)

# Imprimir los atributos del objeto directamente
print(f"Racional 1: {r.numer}/{r.denom}")
print(f"Racional 2: {t.numer}/{t.denom}")
