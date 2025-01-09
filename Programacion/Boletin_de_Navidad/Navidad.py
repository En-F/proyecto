#------------------------------------------------------------------------------------------------
#35
from random import randrange

secreto = randrange(1, 101)
num_intentos = 1 
while True:
    try:
        intento=int(input(f"Introduze el numero secreto(-1 para salir,intento nª{num_intentos}):"))
        if intento == -1:
            break
        if intento == secreto:
            print("HAS ACERTADO")
            break
        if intento < secreto:
            print("El numero secreto es MAYOR")
        else:
            print("El numero secreto es MENOR")
        num_intentos+=1
    except  ValueError:
        print("El dato introducido no es un numero")

#------------------------------------------------------------------------------------------------
#90

from random import randrange
def obtener_entero(prompt: str) -> int:
    """Pide un número entero al usuario y no para hasta que se lo da."""
    while True:
        try:
            res = int(input(prompt))
            return res
        except ValueError:
            print("Dato incorrecto.")

num_digitos = obtener_entero("Introduzca el número de dígitos de la combinación secreta: ")
secreto = [randrange(1,6) for _ in range(num_digitos)]
while True:
    intento = obtener_entero(f"Introduzca la combinación({num_digitos} dígitos): ")
    intento = [int(x) for x in str(intento)]
    if len(intento) != num_digitos:
        print("Número incorrecto de dígitos")
        continue
    if intento == secreto:
        print("Acertaste")
        break
    #for c in intento:
    #    print(c, end=' ')
    print(" ".join(map(str,intento)))
    pistas = []
    for i, s in zip(intento,secreto):
        if i < s:
            pistas.append("<")
        elif i > s:
            pistas.append(">")
        else:
            pistas.append("=")
    print(" ".join(pistas))

#Ejercicio 120
#121. 
import xml.etree.ElementTree as ET 


# Parseamos el archivo 'club.xml' y lo almacenamos en un objeto 'arbol'.
arbol = ET.parse('club.xml')
# Obtenemos la raíz del árbol XML, que es el nodo principal.
raiz = arbol.getroot()
# Recorremos todos los nodos 'socio' que están dentro de 'socios'.
for nodo in raiz.findall("socios/socio"):
    # Obtenemos el valor del atributo 'id' del nodo 'socio' (por ejemplo, '1', '2', etc.).
    ident = nodo.get('id')
    # Buscamos el subelemento 'nombre' dentro del nodo 'socio' y extraemos su contenido de texto.
    nombre = nodo.find("nombre").text
    # Imprimimos el id del socio y su nombre de manera formateada.
    print(f"[{ident}] {nombre}")

#122.
print(len(raiz.findall("socios/socio")))
#devuelve cuántos socios tiene el club , resultado : 2 

#127
d = [['51': ('Winston Churchill', '1942-02-13')],
     ['1':('Sherlock Holmes', '1890-12-14')] ]

lista = []
for nodo in raiz.findall('socios/socio'):
    ident = nodo.get('id')
    nombre = nodo.find("nombre").text       #type: ignore
    alta = nodo.find("alta").text           #type: ignore
    lista.append((alta, ident, nombre ))

lista.sort()

for t  in lista:
    print(t[1:])
    