def histograma(s: str) -> dict[str, int]:
    """Devuelve el histograma de una cadena"""
    res = {}  # Inicializamos un diccionario vacío para almacenar las frecuencias
    for c in s:  # Recorremos cada carácter de la cadena
        if c in res:  # Si el carácter ya está en el diccionario, aumentamos su frecuencia
            res[c] += 1
        else:  # Si no está en el diccionario, lo añadimos con frecuencia 1
            res[c] = 1
    return res  # Devolvemos el diccionario con las frecuencias

# Probamos la función con una cadena de ejemplo
print(histograma("Esto es una prueba de cadena de ejemplo"))


#------------------------------------------------------------------------------------------

def distribucion(s: str) -> dict[str, int]:
    """Devuelve la distribución de repetición de los caracteres de una cadena."""
    res = {}  # Diccionario vacío para almacenar las frecuencias de los caracteres
    for c in s:  # Iteramos sobre cada carácter de la cadena
        if c in res:  # Si el carácter ya está en el diccionario, incrementamos su frecuencia
            res[c] += 1
        else:  # Si el carácter no está en el diccionario, lo agregamos con frecuencia 1
            res[c] = 1
    return res  # Devolvemos el diccionario con las frecuencias de los caracteres


def histograma(s: str) -> None:
    """Dibuja el histograma de una cadena."""
    # Iteramos sobre las claves y valores del diccionario devuelto por distribucion(s)
    for c, n in distribucion(s).items():
        print(c, '=' * n)  # Imprimimos el carácter seguido de n signos '='

# Probamos la función distribucion y la función histograma con una cadena de ejemplo
cadena = "Esto es una prueba de una secuencia de caracteres"
print(distribucion(cadena))  # Muestra el diccionario con las frecuencias
histograma(cadena)  # Muestra el histograma con los caracteres



#------------------------------------------------------------------------------------------
#OTRA VERSION


def morse(mensaje):
    # Diccionario de caracteres a código Morse
    cars_a_puntos = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': ' '
    }
    
    # Inicializamos una lista vacía para guardar los códigos Morse
    res = []
    # Recorremos cada carácter del mensaje en mayúsculas
    for c in mensaje.upper():
        # Si el carácter está en el diccionario, lo agregamos a la lista
        if c in cars_a_puntos:
            res.append(cars_a_puntos[c])
    # Unimos la lista de códigos Morse en una cadena, separada por espacios
    return " ".join(res)

# Ejemplo de uso:
print(morse("HELP ME"))


#------------------------------------------------------------------------------------------

def list2dict(lista: list)-> dict:
    """Devuelve el diccioario equivalente a una lista"""
    res = {}
    for i, e in enumerate(lista):
        res[i] = e
    return res

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def list2dict(lista: list)-> dict:
    """Devuelve el diccioario equivalente a una lista"""
    return {i:e for i, e in enumerate(lista)}
        
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def list2dict(dic: dict)-> list:
    """Recorre un dicionario y devulve una lista"""
    res = [None] * (max(dic) + 1)
    for k, v in dic.items():
        res[k] = v
    return res








""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Ejercicicio de Diccionario
estudiantes = {"Antonio": 9.0, "Paco": 6.0, "Rube": 4.0, "Maria": 9.0, "Mario": 9.5}
def clasificar(estudiantes):
    res = {"Apro": [], "Susp": [], "Sob": []}
    for clave, valor in estudiantes.items():
        if valor >= 9:
            res["Sob"].append(clave)
        elif valor >= 6:
            res["Apro"].append(clave)
        elif valor < 6 :
            res["Susp"].append(clave)
    return res