
#------------------------------------------------------------------------------------------------
#1
try:
    tarea = str(input("¿Has hecho la tarea? (Responde con Sí o No): ")).strip().capitalize()
    tiempo = str(input("¿Está lloviendo? (Responde con Sí o No): ")).strip().capitalize()
    biblioteca = str(input("¿Necesitas ir a la biblioteca? (Responde con Sí o No): ")).strip().capitalize()

    if biblioteca == 'Sí':
        print("Sí, puedes salir a la calle para realizar algún trabajo o entregar un libro.")
    elif tiempo == 'No' and tarea == 'Sí':
        print("Sí, puedes salir a la calle.")
    else:
        print("No, no puedes salir a la calle.")
except ValueError:
    print('Debes introducir un valor correcto ')
#------------------------------------------------------------------------------------------------
#2
try:
    fruta = input('De que fruta tenemos que calcular los beneficios anuales(peras o manzanas):')
    ventas = float(input('Cuales han sido las ventas de una  fruta este ultimo año(en Kilos ):'))

    if fruta == 'peras' and isinstance(ventas, (float, int)):
        operacion = ventas * 1.95
        print(f"Importe total:{round(operacion,2)}")
    elif fruta == 'manzanas' and isinstance(ventas, (float, int)):
        operacion = ventas * 2.35
        print(f"Importe total:{round(operacion,2)}")
except ValueError:
    print('Los valores estan mal introducidos ')
#------------------------------------------------------------------------------------------------
#3
try:
    numero = float(input('Dime un valor: '))
    print(f'El número absoluto es {abs(numero)}')
except ValueError:
    print("¡Error! Debes ingresar un valor numérico válido.")
#------------------------------------------------------------------------------------------------
#4
nota_primer_trimestre = int(input('¿Cuál es la nota del primer trimestre? '))
nota_segundo_trimestre = int(input('¿Cuál es la nota del segundo trimestre? '))
nota_tercer_trimestre = int(input('¿Cuál es la nota del tercer trimestre? '))

notas = [nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre]

nota_media_boletin = sum(notas) // 3  
nota_media_expediente = sum(notas) / 3  


print(f'La nota media del boletín es {nota_media_boletin}, y la nota media del expediente académico es {round(nota_media_expediente,2)}')
#------------------------------------------------------------------------------------------------
#5
try:
    numero = float(input("Dame un numero decimal: "))
    print(f"Numero redondeado al entero más próximo es {round(numero)}")
except ValueError:
    print("¡Error! Debes ingresar un valor numérico válido.")
#------------------------------------------------------------------------------------------------
#6
try:
    # Solicitar la base imponible y el IVA
    base_imponible = float(input("Introduce la base imponible (importe sin IVA): "))
    iva_porcentaje = float(input("Introduce el porcentaje de IVA a aplicar: "))

    iva_importe = (base_imponible * iva_porcentaje) / 100

    total = base_imponible + iva_importe

    print(f"El importe del IVA es: {round(iva_importe,2)}")
    print(f"El total con IVA es: {total}")
except ValueError:
    print("¡Error! Debes ingresar valores numéricos válidos.")

#------------------------------------------------------------------------------------------------
#7
try:
    numero = int(input("Proporcioname un numero: "))

    residuo = numero % 7

    if residuo == 0:
        print("El número ya es múltiplo de 7. No hay que sumarle nada.")
    else:
        cantidad = 7 - residuo
        print(f"A {numero} hay que sumarle {cantidad} para que sea múltiplo de 7.")
    print()
except ValueError:
    print("¡Error! Debes ingresar valores numéricos válidos.")
#------------------------------------------------------------------------------------------------
#8
try:
    n = int(input("Proporcioname un numero: "))
    m = int(input("Proporcioname otro  numero: "))
    residuo = n % m
 
    if residuo == 0:
        print(f"El número {n} ya es múltiplo de {m}. No hay que sumarle nada.")
    else:
        cantidad = m - residuo
        print(f"A {n} hay que sumarle {m} para que sea múltiplo de m.")
    print()
except ValueError:
    print("¡Error! Debes ingresar valores numéricos válidos.")
#------------------------------------------------------------------------------------------------
#9
try:
    base = float(input('Proporcioname la base de un triangulo:'))
    altura = float(input('Proporcioname la altura de un triangulo:'))
    operacion = (base * altura) / 2
    print(f'El area del triangulo de {base} y de {altura} es :{operacion}')
except ValueError:
    print("¡Error! Debes ingresar valores numéricos válidos.")

#------------------------------------------------------------------------------------------------
#10
try:    
    a = float(input('Dame un valor para el coficiente a: '))
    b = float(input('Dame un valor para el coficiente b: '))
    c = float(input('Dame un valor para el coficiente c: '))
    x = int(input('Dame un valor para el coficiente x: '))

    y = pow(a,x) + sum([(b*x),c])

    print(f"Resultado del polinomio de segundo grado donde a={a}, b={b}, c={c}, x={x}:")
    print(f"y = {round(y,2)}")
except ValueError:
    print("¡Error! Debes ingresar valores numéricos válidos.")
#------------------------------------------------------------------------------------------------
#11
unidad_mm = float(input("Dame una medida en milimetros:"))
unidad__cm = float(input("Dame una medida en centrimetros:"))
unidad_m = float(input("Dame una medida en metros:"))

mm_a_cm = unidad_mm / 10
m_a_cm =unidad__cm * 100

total = sum([mm_a_cm,m_a_cm,unidad__cm ])
print(f'El total ha sido {round(total,2)}cm')
#------------------------------------------------------------------------------------------------
#12
hormigas = int(input("¿Cúantas hormigas has capturado?:"))
arañas = int(input("¿Cúantas arañas has capturado?:"))
cochinillas = int(input("¿Cúantas cochinillas has capturado?:"))

patas_hormigas =hormigas * 6 
patas_arañas =arañas * 8 
patas_cochinillas =hormigas * 14 

total = sum([patas_hormigas,patas_arañas,patas_cochinillas])

print(f'El total de patas son de {total}')
#------------------------------------------------------------------------------------------------
#14
entradas_infantil = int(input("¿Cúantas entradas de infantil quieres?:"))
entradas_adultos = int(input("¿Cúantas entradas de adultos quieres?:"))

total_importe = (entradas_infantil * 15.50) + (entradas_adultos * 20)

if total_importe >= 100:
    descuento = total_importe * 0.05
    total_con_descuento= total_importe - descuento
    print(f"A tu compra:{total_importe}€ se le ha colocado un descuento del 5 porciento gracias al bono :{total_con_descuento}€")
else:
    print(f"Tu total a pagar es {total_importe}€")
#------------------------------------------------------------------------------------------------
#15
from math import sqrt
numero = float(input("Proporcioname un numero:"))

if numero < 0 :
    print(f"No se puede realizar la raiz cuadrada con este numero:{numero}, intentelo de nuevo.")
else:
    operacion = sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {operacion}")


import math
numero = float(input("Proporcioname un numero:"))

if numero < 0 :
    print(f"No se puede realizar la raiz cuadrada con este numero:{numero}, intentelo de nuevo.")
else:
    operacion = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {operacion}")

#------------------------------------------------------------------------------------------------
#16
longitud_m = float(input("¿Cúal sido la distancia en metros ?:"))

m_a_cm = longitud_m * 100

print(f"El resultado de tu lanzamiento es de {int(m_a_cm)}cm")
#------------------------------------------------------------------------------------------------
#17
numero = int(input("Dime un numero:"))

if numero % 2 == 0 :
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")
  #------------------------------------------------------------------------------------------------
#18  
numero_1 = int(input("Dime un numero:"))
numero_2 = int(input("Dime otro numero:"))

if numero_1 == numero_2:
    print(f"Los numeros:{numero_1} y {numero_2} son iguales ")
else:
    print(f"Los numeros {numero_1} y {numero_2} no son iguales")
#------------------------------------------------------------------------------------------------
#19
numero_1 = int(input("Dime un numero:"))
numero_2 = int(input("Dime otro numero:"))
try:
    if numero_1 > numero_2:
        print(f"El {numero_1} es mayor que {numero_2}")
    else:
        print(f"El {numero_2} es mayor que {numero_1}")
except ValueError:
    print("El dato introducido no es un numero")
#------------------------------------------------------------------------------------------------
#20
numero_1 = int(input("Dime un numero:"))
numero_2 = int(input("Dime otro numero:"))
try:
    if numero_1 > numero_2:
        print(f"El {numero_1} es mayor que {numero_2}")
    elif numero_1 == numero_2:
        print(f"Los numeros:{numero_1} y {numero_2} son iguales")
    else:
        print(f"El {numero_2} es mayor que {numero_1}")
except ValueError:
    print("El dato introducido no es un numero")
#------------------------------------------------------------------------------------------------
#21
numero_1 = float(input("Dime un numero decimal :"))

if -1 < numero_1 < 1 and numero_1 != 0:
    print(f"El {numero_1} es casi-cero")
else:
    print(f"El {numero_1} no es  casi-cero")
#------------------------------------------------------------------------------------------------
#22
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


if numero1 > numero2:
    print(f"{numero1}, {numero2}")
else:
    print(f"{numero2}, {numero1}")


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


numeros = [numero1, numero2]
numeros_ordenados = sorted(numeros, reverse=True)

print(f"Los números ordenados en orden decreciente son: {numeros_ordenados[0]}, {numeros_ordenados[1]}")

#------------------------------------------------------------------------------------------------
#23
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

numeros = [numero1,numero2,numero3]
numeros_ordenados = sorted(numeros, reverse=True)

print(f'Los numeros ordenados son {numeros_ordenados}')
#------------------------------------------------------------------------------------------------
#24
from math import sqrt
a = float(input("Dame el valor para a en la ecuacion de segundo grado:"))
b = float(input("Dame el valor para b en la ecuacion de segundo grado:"))
c = float(input("Dame el valor para c en la ecuacion de segundo grado:"))

x = (-b + sqrt(pow(b,2) - 4*a*c)) / (2 * a)


print(f"El resultado de la operacion es {x}")
#------------------------------------------------------------------------------------------------
#25
numero = int(input("Dime un numero:"))
if 0 < numero < 99999:
    cifras = len(str(numero))
    print(f"El {numero} tiene {cifras} cifras")
else:
    print("El número no está en el rango permitido (0 < número < 99999).")
#------------------------------------------------------------------------------------------------
#26

nota = float(input("Dime la nota que has sacado en el examen: "))

if 0 < nota < 4.0:
    print("Insuficiente")
elif nota == 5.0:
    print("Suficiente")
elif nota == 6.0 :
    print("Bien")
elif  nota == 7.0 and  8.0:
    print("Notable")
elif nota == 9.0:
    print("Notable")
elif nota == 10.0:
    print("Matrícula de honor")
#------------------------------------------------------------------------------------------------
#27

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
    
#96
l = [10, 1, 5, 8, 9, 2]

def consecutivo(lst, d):
    g = []
    while len(lst) >= d:  # Mientras haya suficientes elementos para tomar subsecuencias de tamaño 'd'
        t = sum(lst[0:d])  # Sumar los primeros 'd' elementos
        g.append(t)  # Agregar la suma de la subsecuencia a la lista 'g'
        lst = lst[1:]  # Eliminar el primer elemento para obtener la siguiente subsecuencia
    
    print(g)  # Imprimir el resultado final con las sumas de las subsecuencias

# Llamar a la función
consecutivo(l, 3)

#101
password = input("Introduce la contraseña:")

while True:
    intento = input("Introduzla la  palabras:")
    for i,e in enumerate(password):
        if i < len(intento):
            print("*", end='')          
        elif intento[i] != e:   #no coincide
            print("*", end='')
        elif intento[i] == e :
            print("*", end='')
    print()
    if intento == password:
        break
                

#Ejercicio 120 
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


for nota in raiz.iter('nota'):
    
    nueva_nota = int(nota.text) + 1
    nota.text = str(nueva_nota)
    nota.set('modificado', 'si')

    arbol.write('salida.xml')
   
#123
import xml.etree.ElementTree as ET

# Parsear el archivo XML
arbol = ET.parse('club.xml')
raiz = arbol.getroot()

# Buscar las direcciones de los socios y modificar su texto
for direccion in raiz.findall(".//socios/socio/direccion"):
    direccion.text = "Avda. de Huelva, s/n"

# Guardar los cambios en el archivo XML
arbol.write("club.xml", encoding="utf-8", xml_declaration=True)



#124
import xml.etree.ElementTree as ET

# Parsear el archivo XML
arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

# Buscar el elemento <direccion> donde el atributo 'id' del socio es "1"
direccion = raiz.find("socios/socio[@id='1']/direccion")

# Verificar si se encontró el elemento y actualizar su texto
if direccion is not None:
    direccion.text = "Calle Ancha, 35"

# Guardar los cambios en un nuevo archivo XML
arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)


#125
import xml.etree.ElementTree as ET

# Parsear el archivo XML
arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

# Buscar el socio con id '51'
socio = raiz.find("socios/socio[@id='51']")

# Verificar si el socio fue encontrado antes de eliminarlo
if socio is not None:
    # Obtener el elemento <socios> y eliminar el socio encontrado
    socios = raiz.find("socios")
    socios.remove(socio)

# Guardar los cambios en un nuevo archivo XML
arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)

#126
import xml.etree.ElementTree as ET

arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

socio = raiz.find("socios/socio[@id='1']")
telefono = ET.SubElement(socio/'telefono')
telefono.text = "666555444"

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)

#127
import xml.etree.ElementTree as ET

arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()
for nodo in raiz.findall("socios/socio"):
    ident = nodo.get("id")
    nombre = nodo.find("nombre").text
    print()

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)



