class Animal:
    def comer(self):
        return("Estoy comiendo")

class Mamifero(Animal):
    def amamantar(self):
        return("Estoy amamantando")

class Ave(Animal):
    def volar(self):
        return("Estoy volando")

class Murciegalo(Mamifero,Ave):
    pass


murciegalo = Murciegalo()
ave = Ave()

print(ave.volar())
print(ave.comer())

print(Murciegalo.mro())