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
    res = {}  # Inicializamos un diccionario vacío para almacenar las frecuencias de cada carácter
    for c in s:  # Iteramos sobre cada carácter de la cadena
        if c in res:  # Si el carácter ya está en el diccionario, incrementamos su frecuencia
            res[c] += 1
        else:  # Si el carácter no está en el diccionario, lo añadimos con frecuencia 1
            res[c] = 1
    return res  # Devolvemos el diccionario con las frecuencias de los caracteres

def histograma(s: str) -> None:
    """Dibuja el histograma de una cadena."""
    dist = distribucion(s)  # Llamamos a la función distribucion para obtener las frecuencias de los caracteres
    for c in dist:  # Recorremos cada clave (carácter) en el diccionario de frecuencias
        n = dist[c]  # Obtenemos la frecuencia del carácter
        print(c, '=' * n)  # Imprimimos el carácter seguido de una cantidad de '=' igual a su frecuencia

# Probamos la función histograma con una cadena de ejemplo
histograma("Esto es una prueba de una secuencia de caracteres")
