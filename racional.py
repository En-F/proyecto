class Racional:
    # El método __init__ es el constructor de la clase, donde inicializamos los atributos del objeto.
    def __init__(self, num, den):
        self.numer = num  # Atributo para el numerador de la fracción.
        self.denom = den  # Atributo para el denominador de la fracción.
    # Método para obtener el numerador del objeto racional.
    def numerador(self):
        return self.numer  # Devuelve el valor del numerador.    
    # Método para obtener el denominador del objeto racional.
    def denominador(self):
        return self.denom  # Devuelve el valor del denominador.
    # Método para multiplicar dos objetos de tipo Racional.
    def mult(self, otro):
        # Calculamos el numerador del resultado multiplicando los numeradores de ambos objetos.
        n = self.numerador() * otro.numerador()
        # Calculamos el denominador del resultado multiplicando los denominadores de ambos objetos.
        d = self.denominador() * otro.denominador()
        # Retornamos un nuevo objeto Racional con el numerador y denominador resultantes.
        return Racional(n, d)

# Crear dos objetos de la clase Racional con los valores 3/4 y 5/6.
r = Racional(3, 4)
t = Racional(5, 6)

# Imprimir los atributos 'numer' y 'denom' de los objetos r y t.
# Se usa f-string para formatear la salida y mostrar la fracción.
print(f"Racional 1: {r.numer}/{r.denom}")  # Muestra la fracción del primer objeto.
print(f"Racional 2: {t.numer}/{t.denom}")  # Muestra la fracción del segundo objeto.



