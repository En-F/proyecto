edad = int(input("Dame  un numero: "));

'Alevín' if  edad < 7 else  \
'Benjamín' if edad < 12  else \
'Junior' if edad < 17 else \
'Sénior'

# #Se le conoce como  SENTENCIA porque no devuelve un resultado
# #De primera mano se llama Bing y si se rompe  la variable se le llama rebinding
# #Se le denomina definición, (darle un nombre a un valor que ya existe)
# #Se crea ligadura entre el nombre(identificador[obligatorio que empieze por una letra]) y el valor ,  en este caso se representa edad ---> 20

# #----------------------------------s

# # max ---> λ
# # len ---> λ

# #Todas estas variables se guarda en  la memoria Principal

# #----------------------------------
# #Esto tenemos que hacer para comparar tres numeros  en un script
a = 5
b = 5
c = 5
iguales = a == b and b == c
print(iguales)

 #----------------------------------
#El programa se encarga de calcular el mayor y el menor de dos numeros que pide el usurio por teclado.

numero_1 = int(input('Dame un número: '))
numero_2 = int(input('Dame otro número: '))

if numero_1 > numero_2:
    print('El número más grande es:', numero_1)
    print('El número más pequeño es:', numero_2)
elif numero_1 < numero_2:
    print('El número más grande es:', numero_2)
    print('El número más pequeño es:', numero_1)
else:
    print('Ambos números son iguales')




#--------------------------------------------------------------------------------------
#Ejercicio 9 EN PROGRAMA 
#Escribir un programa que reciba dos datos de entrada y que los ordene de menor a
#mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

a=5
b=2
menor=min(a ,b )
mayor=max(a, b,)
print('El numero mas grande es:',mayor,'y el numero mas pequeño es:',menor)

#Ejercicio 9 EN FUNCION
#Escribir un programa que reciba dos datos de entrada y que los ordene de menor a
#mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.
mayor_de_numeros =lambda a, b:(min(a, b) and max(a, b))

print('El numero mas grande es:',mayor,'y el numero mas pequeño es:',menor)
# #Si ha esta esta entre primero y tercero devulve a y si b entre primero y tercero devuelve b si no else

#--------------------------------------------------------------------------------------

#Ejercicio 10
#Escribir un programa que reciba tres datos de entrada y que los ordene de menor a
#mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

a=5
b=2
c=4
primero=min(a ,b ,c)
tercero=max(a, b, c)
#Si ha esta esta entre primero y tercero devulve a y si b entre primero y tercero devuelve b si no else
segundo= a if primero < a and a < tercero else b if primero < b and b < tercero else c
#--------------------------------------------------------------------------------------

#EJERCICIO 11
#Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
#enteros, de dos formas diferentes:
#a) Mediante la función lcm del módulo math.
#b) Aprovechando la siguiente propiedad:
    #𝑎 · 𝑏 = 𝑚𝑐𝑑 (𝑎, 𝑏) · 𝑚𝑐𝑚(𝑎, 𝑏)

from math import lcm
a = int(input('Dame un número: '))
b = int(input('Dame otro número: '))
mcm = lcm(a ,b)
print('El numero es:',mcm)

#b) Aprovechando la siguiente propiedad:

from math import gcd

a = int(input('Dame un número: '))
b = int(input('Dame otro número: '))
mcd= gcd(a,b)
mcm = (a * b)// mcd
print(mcm)

#------------------------------------------------------------------------------

#EJERCICIO 12
#Escribir un programa que quite todos los espacios en blanco que se encuentren dentro de
#una cadena. 
#La salida será la cadena de entrada pero sin los espacios en blanco. 
#Por ejemplo, ante la entrada "Esto es una prueba" la salida debería ser "Estoesunaprueba".
entrada = 'Esto es una prueba'
sin_espacios=entrada.replace(' ','')
print(sin_espacios)

#EJERCICIO 12 EN FORMA DE FUNCION
#Escribir un programa que quite todos los espacios en blanco que se encuentren dentro de
#una cadena. 
#La salida será la cadena de entrada pero sin los espacios en blanco. 
#Por ejemplo, ante la entrada "Esto es una prueba" la salida debería ser "Estoesunaprueba".
quita_espacios=lambda s:s.replace(" ","")
quita_espacios("Esto es una prueba")
print(quita_espacios)

#------------------------------------------------------------------------------

#Escribir un programa que diga si dos cadenas son iguales sin tener en cuenta las
#mayúsculas y minúsculas. Por ejemplo, el programa debería decir que las cadenas
#"Hola" y "hoLa" son iguales
x = str(input('Dame una cadena : ')).upper()
y = str(input('Dame otra cadena : ')).upper()

if x == y:
    print('True')
elif x != y:
     print('False')


#------------------------------------------------------------------------------

#Escribir una función que implemente la siguiente especificación:

#(Que implemente la siguiente  especificacion) es que satisfaga las necesidades que se te pide
# PRECONDICION(reponsabilidad del que llama):
#  𝑛 ≥ 0
# POST CONDICION(respondabilidad del que crea la funcion):
#   repite(𝑠: str, 𝑛: int) -> str
#Post : repite(𝑠) = 𝑠 repetido 𝑛 veces

repite = lambda s, n:(s * n)
repite("Hola",5)
print(repite)

#------------------------------------------------------------------------------
#EJERCICIO 6 DEL TEMA Programación funcional (I) EN FUNCION

from math import pi
radio= 2.0
volumen= lambda r:(4 / 3) * pi * (r ** 3)
print(volumen)

#------------------------------------------------------------------------------
#EJERCICIO 7 DEL TEMA Programación funcional (I) EN FORMA DE FUNCION
a = 2
b = 2
c = 4
iguales = lambda a, b, c: (a == b and b == c)
resultado = True

#EJERCICIO 7 DEL TEMA Programación funcional (I) EN FORMA DE PROGRAMA
a = 2
b = 2
c = 4
iguales = True if a == b and b == c else False
resultado = True

#------------------------------------------------------------------------------
#EJERCICIO 8 DEL TEMA Programación funcional (I) EN FORMA DE FUNCION
a = 2
b = 2
c = 4
d = 4
iguales = lambda a, b, c, d: (a == b and b == c and c ==d)
resultado = True

#EJERCICIO 8 DEL TEMA Programación funcional (I) EN FORMA DE PROGRAMA
a = 2
b = 2
c = 4
d = 4
iguales = True if a == b and b == c and c ==d else False
resultado = True

#------------------------------------------------------------------------------
r = 25
suma = lambda x, y:(x +y )
resultado = suma(r, 4)

#------------------------------------------------------------------------------
# Escribir una función calculadora a la que se le pasan dos números reales y qué operación se desea realizar con ellos. 
# Las operaciones disponibles son: sumar, restar, multiplicar o dividir. Éstas se especifican mediante un carácter: '+', '-', '*' o '/', respectivamente.
# La función devolverá el resultado de la operación en forma de número
# real.
#op es el operador que vamos a utilizar
calculadora = lambda x, y, op:  x + y if op==  "+" else\
                                x - y if op==  "-" else\
                                x * y if op == "*" else\
                                x / y if op == "/" else "Error"
#------------------------------------------------------------------------------

# Escribir una función que reciba dos instantes de tiempo en forma de horas y minutos y
# que cumpla con la siguiente especificación:
# 
# Pre : ℎ𝑜𝑟𝑎1 ≥ 0 ∧ 𝑚𝑖𝑛𝑢𝑡𝑜1 ≥ 0 ∧ ℎ𝑜𝑟𝑎2 ≥ 0 ∧ 𝑚𝑖𝑛𝑢𝑡𝑜2 ≥ 0
#           distancia(ℎ𝑜𝑟𝑎1: int, 𝑚𝑖𝑛𝑢𝑡𝑜1: int, ℎ𝑜𝑟𝑎2: int, 𝑚𝑖𝑛𝑢𝑡𝑜2: int) -> int
# Post : distancia(ℎ𝑜𝑟𝑎1, 𝑚𝑖𝑛𝑢𝑡𝑜1, ℎ𝑜𝑟𝑎2, 𝑚𝑖𝑛𝑢𝑡𝑜2) =
#          la cantidad de minutos que existen de diferencia entre los dos instantes
# Dar un ejemplo de uso

distancia = lambda hora1, minuto1, hora2,minuto2:\
    (60 * hora1 + minuto1) + (hora2 * 60 +minuto2)
print(distancia(23, 12, 15, 59))

#------------------------------------------------------------------------------
#EJERICIO 5 TEMA 3 Programación funcional (I)


altura = lambda sexo, edad, lingitud_tibia:'Hombre' if 69.080 +2.232 * lingitud_tibia else\
                                   'Mujer' if  61.412 + 2.317 * lingitud_tibia else 'Error'



#------------------------------------------------------------------------------
#
# IMPLEMENTACION RECURSIVA DE LA FUNCION FACTORIAL
# ESTO ES LA ESPECIFICACION: FOTO DOCUMENTACION
#    Pre:n>=0
#       factorial(n:int) ---> int
#   Post: factorial(n)=n!
#  CUANDO HACEMOS LO QUE NOS DICE EL PROGRAMA QUE HAGA SE LE LLAMA IMPLEMENTACION:
# 
factorial = lambda n:1 if n==0 else \
                    n * factorial(n-1)
print(factorial(5))

#------------------------------------------------------------------------------
#FUNCIONES RECURSIVAS
sumatorio = lambda n:0 if n==0 else \
                    n * sumatorio(n-1)
print(sumatorio(5))


# #------------------------------------------------------------------------------
# TEMA DE PROGRAMACION FUNCIONA(II)
# 2. La función potencia tiene la siguiente especificación:
#   Pre : 𝑏 ≥ 0
#       potencia(𝑎: int, 𝑏: int) -> int
#   Post : potencia(𝑎, 𝑏) = 𝑎
# 
# a) Implementar la función de forma no recursiva.
potencia = lambda a,b : a**b #igual que la funcion pow
potencia(a,0)=1 #caso base ya que cualquier numero elevar a 0 da uno 
potencia(a,b), b>0 # no estamos e al caso base, tenemos que converteirlo en un caso entre 0
# y b para que el segundo se acerque a al caso base para ello le restamos uno
# a la b el caso que no es base es decir, lo que estasmo haciendo es reducir 
potencia(a,b-1)
#tenemos potencia(2,5), esto no lo sabemos hacer para ello tendriamos que saber hacer la potencia(2,4)
#  tenemos 2⁵ = 2 * 2⁴
#a^b = a * a^b-1 conocido como hipotesis de inducción
# (echo de que tu supones que sbes resolver ejemplares que se encuatran mas cerca del caso base)
# b) Implementar la función de forma recursiva
#              | 1,   b=0
#potencia(a,b) |
#              | a* potencia(a,b-1), b>0
# potencia(2,3)
# 2 * potencia(2,2)
# 2 * 2 *potencia(2,1)
# 2 *2 * 2potencia(2,0)
# 2 * 2 * 2 * 1 
# = 8:int

#------------------------------------------------------------------------------
# Pre :True
#      longitud(s:srt)---> int
#Post longitud(s:srt)= nª de caracteres de s.
#
# a) Implementar la función de forma no recursiva.:
# longitud= len(s)
#
#longitud('') = 0  esto seria el caso base
# ahora vamos a crear una funcion  que se parece  al caso base 
# longitud('')=0     longitud('Hola')
#                    'hola'[1:] = 'ola'
#tenemos longitud('Hola'), esto no lo sabemos hacer para ello tendriamos que saber hacer la longitud('ola')
#  tenemos 4 = 1 + 3
#l('hola')
#l + 1('ola')
#l + 1 + 1('la')
#l +1 +1 +1('hola')
#l('hola')
#l('hola')
#b) Implementar la función de forma recursiva
#              | 0 , s = ''
#longgitud(s   |
#              | 1 + longitud(s[1:])  s =¡''


# La función repite tiene la siguiente especificación:
# Pre : 𝑛 ≥ 0
#   repite(𝑠: str, 𝑛: int) -> str
# Post : repite(𝑠, 𝑛) = 𝑠 * n
#a) Implementar la función de forma no recursiva:
#repite (s,n) = s * n
repite ('a',5) = 'aaaaa' 
potencia(s,0)=''
potencia(s,n-1)=1
#tenemos repite ('aaaaa') = 'aaaaa', esto no lo sabemos hacer para ello tendriamos que saber hacer la longitud('aaaa')
#  tenemos 5 = 1 + 4
repite = lambda s,n: '' if n== 0 else s + repite (s,n-1)
#------------------------------------------------------------------------------
# la suma de todos lo numeors enteros comprendidos entre i y j
suma = lambda i,j: 0 if i > j else suma(i,j-1) + j
suma(4,6)
#------------------------------------------------------------------------------
# Pre : 𝑛 ≥ 0
#   digito:(𝑛: int) -> int
# Post : digito(𝑛) =  el nª de digitos de n

digito = lambda n: len(str(n))#Esta es la  no recursiva

digito = lambda n: 1 if 10 > n else 1 + digito(n // 10)# Para poder quitarle un digito al anterior tenemos que hacer una division entera(//), por que con l division normal  nos daria un float.s
    
#------------------------------------------------------------------------------
# 5. La función suma_digitos calcula la suma de los dígitos de un número entero:
# suma_digitos(423) = 4 + 2 + 3 = 9
# suma_digitos(7) = 7
# Se pide:
# a) Escribir su especificación.
# Pre : 𝑛 ≥ 0
#   suma_digito:(𝑛: int) -> int
# Post : suma_digito(n)=   la sima de los digitos e n
#  b) Implementar una función recursiva que satisfaga dicha especificación.
suma_digito = lambda n: n if 10 > n else (n % 10) + suma_digito(n // 10)
# Indicación: Recordar que n // 10 le quita el último dígito a 𝑛. Además, n % 10 devuelve
# el último dígito de 𝑛.

#------------------------------------------------------------------------------
# La función voltea le da la vuelta a un número entero:
# voltea(423) = 324
# voltea(7) = 7
# Se pide:
# a) Escribir su especificación.
# Pre : 𝑛 ≥ 0
#   voltea:(𝑛: int) -> int
# Post : voltea(n)= coloca n en orden contrario
# b) Implementar una función recursiva que satisfaga dicha especificación.
# Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
# entero. Usar además la indicación del ejercicio anterior.

#------------------------------------------------------------------------------
suma = lambda t:0 if t == () else t[0]+ suma(t[1:]) #Cuaderno
#------------------------------------------------------------------------------
longitud = lambda t:0 if t == () else 1+ longitud(t[1:])
#------------------------------------------------------------------------------
mitad  = lambda t:0 if t == () else (t[0]/2,) + mitad(t[1:])
#------------------------------------------------------------------------------
redondear  = lambda t:0 if t == () else (round(t[0]),) + redondear(t[1:])
#------------------------------------------------------------------------------
intervalo=  lambda i, j:() if i>j else (i,) + intervalo(i+1,j)
cuadrado = lambda t: tuple(map(lambda x: x ** 2, t))
suma = lambda t:0 if t == () else t[0]+ suma(t[1:])
#Si sumamos todos las funciones nos da lo siguiente:#para realiar la funcion tenemos que ordenarlo al contrario,(suma>cuadrado>intervalo)
suma_cuadrado = lambda i, j:suma(cuadrado(intervalo(i, j)))

intervalo=  lambda i, j:tuple(range(i, j+1)) 

from functools import reduce
factorial = lambda n: reduce(lambda x,y :x * y ,range(1,n+1),1)

#------------------------------------------------------------------------------
# La función potencia tiene la siguiente especificación:
# Pre : 𝑏 ≥ 0
#   potencia(𝑎: int, 𝑏: int) -> int
# Post : potencia(𝑎, 𝑏) = 𝑎
# a) Implementar la función de forma no recursiva.
# b) Implementar la función de forma recursiva.
#tambien se puede implemetar la operacion mul( que reliza la multilicacion de dos numeros)
from operator  import mul
potencia = lambda a,b: reduce(lambda acc, y :acc  *  y,(a,) * b, 1)
potencia = lambda a,b: reduce(mul,(a,) * b, 1)
potencia(2,3) # el resultado da ( 8 )>>>


#------------------------------------------------------------------------------
# La función mayor tiene la siguiente especificación:
# Pre : 𝑡 ≠ ()
#   mayor(𝑡: tuple[𝛼]) -> 𝛼
# Post : mayor(𝑡) = el mayor elemento de 𝑡
# Por ejemplo: mayor((3, 2, 5, 7)) == 7.
# Escribir una función recursiva que satisfaga dicha especificación.
from functools import reduce
max2 = lambda x,y: x if x > y else y
mayor = lambda t:reduce(max2 ,t,1)
#------------------------------------------------------------------------------
#Expresiones generadoras
( x ** 2 for x in (1,2,3,4,5))
tuple( x  for x in range(1, 21) if  x % 2 == 0)
#Dame todos los numeors que se encuantren el rango y sean pares
#------------------------------------------------------------------------------
es_primo= lambda n: all(n % x != 0 for x in range(2,n)) 
#La x va cambiando y se va desplazando por todos los numoro execto el n

divisores_n= lambda n: len(tuple( x  for x in range(2,n) if n % x == 0)) == 0 

es_primo= lambda n: len(divisores_n(n)) == 2
#------------------------------------------------------------------------------
a = int(input("Dame un numero:"))
b = int(input("Dame otro numero:"))
suma = a + b
print("La suma de ", a, "y", b, "es:",suma, end='\n')
print (" Buenas noches")

#------------------------------------------------------------------------------
#Imperativo
# 10. Escribe un programa que calcule la media aritmética de dos notas enteras. Hay que
# teneren cuenta que la media puede contener decimales.
nota_1=  float(input("Dame la nota del primer examen:"))
nota_2=  float(input("Dame la nota del primer examen:"))
nota_aritmetica=(nota_1 + nota_2) / 2.0
print("La nota media es :",nota_aritmetica)

#------------------------------------------------------------------------------
#Imperativo
# 11. Escribe un programa que calcule la longitud y el área de una circunferencia. Para ello,
# el usuario debe introducir el radio (que puede contener decimales).
# Recordemos:
# 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜
# 𝑎𝑟𝑒𝑎 ´ = 𝜋 · 𝑟𝑎𝑑𝑖𝑜2
from math import pi
radio = float(input("Dame el radio de una circunferencia:"))
longitud=  (2 * pi) * radio
area=  pi * radio**2
print("La longitud de la circunferencia es:", round(longitud,3))
print("El area es:",round(area,3))

#------------------------------------------------------------------------------
#Escribe un programa que pida al usuaro un numero que represente un año y determine si ese ño es bisisesto o no.
anyo = int(input("Dame un año: "))

p= anyo % 4 == 0
q = anyo % 100 == 0
r = anyo % 400 == 0

if (p and not q) or r :
    print("Si")
else:
    print("No")

#Otro ejemplo;
anyo = int(input("Dame un año: "))
if anyo % 4 == 0 :
    if anyo % 100 !=0 :
        print("Si")
    else:
        if anyo % 100 ==0 :
            print("Si")
        else:
            print("No")
else:
    if anyo % 4 == 0:
        print("Si")
    else:
        print("No")

#------------------------------------------------------------------------------

# Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
# joven!» si es menor de 25 años y «No está mal.» si tiene entre 25 y 40 años.
edad = int(input("Dame tu edad: "))
if edad < 25:
    print("¡Qué joven!")
elif edad <= 40:
    print("No está mal.")
else:
    print("Estás muy mal.")

#otra opcion
if edad < 25:
    print("¡Qué joven!")
else:
    if edad <= 40:
        print("No está mal.")
    else:
        print("Estás muy mal.")
#------------------------------------------------------------------------------
#PROGRAMACION ESTRUCTURADA
#6. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
#comprendido entre 0 y 10, intrsoducido por teclado.

numero=int(input("Introduzca el número de la tabla deseada(entre 0 y 10): "))
i = 0
if numero >= 0 and numero <= 10:
    while i <= 10 :
        print(numero, "X" ,i, "=" , numero * i)
        i +=1
else:
    print("El numero no esta entre los limites solicitados")

#A RICARDO LE GUSTA ESTA OPCION
numero=int(input("Introduzca el número de la tabla deseada(entre 0 y 10): "))
if numero < 0 or numero > 10:
    print("El numero no esta entre los limites solicitados")
else:
    i = 0
    while i <= 10 :
        print(numero, "X" ,i, "=" , numero * i)
        i +=1
#A OTRA OPCION
numero=int(input("Introduzca el número de la tabla deseada(entre 0 y 10): "))
if numero not in range(11):
    print("El numero no esta entre los limites solicitados")
else:
    i = 0
    while i <= 10 :
        print(numero, "X" ,i, "=" , numero * i)
        i +=1

#------------------------------------------------------------------------------
#Un ejemplo  para que el usurrio mete un numero erroneo tenga mas oportunidades
salir = False #inteructor
while not salir:
    numero=int(input("Introduzca el número de la tabla deseada(entre 0 y 10): "))
    if numero not in range(11):
        print("El numero no esta entre los limites solicitados")
    else:
        salir = True

i = 0

while i <= 10 :
    print(numero, "X" ,i, "=" , numero * i)
    i +=1

#En este ejemplo hemos utilizado el break

while True:
    numero=int(input("Introduzca el número de la tabla deseada(entre 0 y 10): "))
    if numero  in range(11):
        break # nos ahorramoe  el else,  si cumple con la condicion se va al break, y si no se cumple no se ejecuta el break y pasa directamente al print()
    print("El numero no esta entre los limites solicitados")
     
i = 0

while i <= 10 :
    print(numero, "X" ,i, "=" , numero * i)
    i +=1
#------------------------------------------------------------------------------
#PROGRAMACION IMPERATIVA
# 17. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
# introducidos por teclado.

#OTRA OPCION ( mas elegante para ricardo)
lista = []
while len(lista) < 5:
    n=float(input("Introduzca un numero real: "))
    lista.append(n)
if len(lista) == 5:
    media = sum(lista)/len(lista)
    print("La media es ", media)
    
#OTRA OPCION ( mas elegante para ricardo)
CANTIDAD= 5
lista = []
while len(lista) < CANTIDAD:
    n=float(input("Introduzca un numero real: "))
    lista.append(n)
media = sum(lista)/CANTIDAD
print("La media es ", media)
    
#OTRA OPCION(mas eficiente para ricardo, funciona con mas cantidad de numeros)

CANTIDAD= 5
suma = sum(float(input("Introduzca un numero real: ")) for _ in range(CANTIDAD))
media = suma / CANTIDAD
print("La media es ", media)


#------------------------------------------------------------------------------

#9. ESTRUCTURA  ESTRUCTURADA
#Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
#luego las muestre en orden inverso a como se han introducido, desde la última cadena
#introducida hasta la primera.
lista= []
while len(lista) < 10 :
    lista.append(input("Dame un palabra: " ))

invertida = lista[::-1]

i = 0
while i < 10:
    print(invertida[i])
    i+=1

#OTRO EJEMPLO( NO ES LO QUE PIDE EL ENUNCIADO)
lista= []
while len(lista) < 10 :
    lista.append(input("Dame un palabra: " ))
    
while  len(lista) > 0 :
    print(lista.pop())


#OTRO EJEMPLO
lista= []
while len(lista) < 10 :
    lista.append(input("Dame un palabra: " ))

i = len(lista) -1
while  i >=  1 :
    print(lista[1])
    i -= 1
#------------------------------------------------------------------------------
from math import pi

while True:     
    try:
        radio = float(input("Dame el radio de una circunferencia:"))
        break
    except ValueError:
        print("Error:se ha producido un error")
            
longitud=  (2 * pi) * radio
area=  pi * radio**2
print("La longitud de la circunferencia es:", round(longitud,3))
print("El area es:",round(area,3))


#------------------------------------------------------------------------------
from math import pi
try:
    anyo = int(input("Dame un año: "))
    p= anyo % 4 == 0
    q = anyo % 100 == 0
    r = anyo % 400 == 0
    if (p and not q) or r :
        print("Si")
    else:
        print("No")
except ValueError:
    print("Error: se ha producido un valor incorrecto.")
#------------------------------------------------------------------------------
CANTIDAD = 5
def obtener_numero_real():
        while True:
            try:
                n=float(input("Introduzca un numero real: "))
                break
            except ValueError:
                print("Valor Incorrecto:Vuelve a intentarlo")
        return n


lista = []
while len(lista) < CANTIDAD:
    n = obtener_numero_real()
    lista.append(n)
media = sum(lista)/CANTIDAD
print("La media es ", media)

#------------------------------------------------------------------------------
def fatorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n - 1)

"""
Implementacion imperativa de la funcion factorial usando bucles
"""
def factorial(n):
    res = 1
    while n >= 1:
        res *= n
        n-= 1
    return res

print(factorial(0))

#------------------------------------------------------------------------------
def mostrar_menu():
    """ Muestra el menú"""
    print(
    """
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.
    """
    )

def elegir_opcion():
    """Pide al usuario la opción que desea"""
    return input("Elija la opción que desee: ")

def anyadir_elemento(lista):
    """Añade un elemento a la lista"""
    elemento = input("Introduce el elemento a añadir: ")
    lista.append(elemento)
    print(f"Elemento se ha  añadido a la lista correctamente.",elemento)

def cambiar_elemento(lista):
    """Cambia  el  elemento  de  la lista por otro """
    try:
        indice = int(input("Introduce el índice del elemento a cambiar: "))
        nuevo_elemento = input("Introduce el elemento nuevo: ")
        lista[indice] = nuevo_elemento
    except ValueError:
        print("El índice introducido no es un número")
    except IndexError:
        print("Por favor, introduce un índice válido.")

def eliminar_elemento(lista):
    """Elimina un elemento de la lista"""
    elemento = input("Introduce el elemento a eliminar: ")
    if elemento in lista: 
        lista.remove(elemento)
        print("Elemento se ha  eliminado de la lista.")
    else:
        print("El elemento  no se encuentra en la lista.")

def eliminar_todos(lista):
    """Elimina todos los elementos de la lista"""
    lista.clear()
    print("Todos los elementos han sido eliminados de la lista.")

def mostrar_todos(lista):
    """Muestra los elementos de la lista"""
    return print(lista)
""" 
Si no se puediera hacer el print(lsita) pues tenemos que hacer lo siguiente
lista = ["1", "2", "3", "4"]
"el separador entre elemento es la , y el espacio"

print("[" + ", ".join(lista) + "]") 
"""

# Lista inicial vacía
lista = []
while True:
    mostrar_menu()
    opc = elegir_opcion()
    if opc == "1":
        anyadir_elemento(lista)
    elif opc == "2":
        cambiar_elemento(lista)
    elif opc == "3":
        eliminar_elemento(lista)
    elif opc == "4":
        eliminar_todos(lista)
    elif opc == "5":
        mostrar_todos(lista)
    elif opc == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")

#------------------------------------------------------------------------------
# En el programa, los cuatro empleados que tiene la empresa se almacenan en la siguiente
# lista:
empleados = [('María', 'González', 1800.23),
    ('Javier', 'Ruiz', 1630.50),
    ('Jesús', 'Pérez', 2100.42),
    ('Rosa', 'Muñoz', 2240.78)]
# Se pide escribir un programa que modifique la lista de empleados incrementando en un
# 10 % el salario de cada empleado y muestre por pantalla el salario total de los empleados
# de la empresa.

# Lista de empleados, donde cada tupla contiene (nombre, apellido, salario)
empleados = [('María', 'González', 1800.23),
             ('Javier', 'Ruiz', 1630.50),
             ('Jesús', 'Pérez', 2100.42),
             ('Rosa', 'Muñoz', 2240.78)
]

# Variable para acumular el total de los salarios después del aumento
suma = 0

# Iterar sobre cada empleado usando 'enumerate' para obtener índice 'i' y los datos de cada empleado 'emple'
for i, emple in enumerate(empleados):
    # Desempaquetar la tupla en nombre, apellido y salario
    nombre, apellido, salario = emple
    
    nuevo = (nombre, apellido, salario )
    
    # Redondear el salario aumentado a 2 decimales
    salario = round(salario * 1.10, 2)
    
    # Reemplazar la tupla en la lista de empleados con el nuevo salario
    empleados[i] = nuevo
    
    # Imprimir los datos del empleado con el nuevo salario
    print("empleado", nombre, apellido, "con salario", salario)
    
    # Acumular el nuevo salario en la variable 'suma'
    suma += salario
    
# Imprimir la suma total de todos los salarios aumentados
print("Salario total es", suma)

#------------------------------------------------------------------------------
def emparejar(lista: list) -> list:
    res = []  # Inicializamos una lista vacía donde almacenaremos los resultados
    for e in lista:  # Iteramos sobre cada elemento en la lista
        res.append((0, e))  # Emparejamos el elemento con el valor 0 y lo agregamos a 'res'
    return res  # Retornamos la lista de tuplas con el valor (0, elemento)

# Ejemplo de uso
print(emparejar(['a', 'b', 'c', 'd']))

#OTRA

def emparejar(lista: list) -> list:
    return [(0, x ) for x in lista]
print(emparejar(['a', 'b', 'c', 'd']))

#------------------------------------------------------------------------------
def emparejar(lista: list) -> list:
    return [(i, e) for i, e in enumerate(lista, )]  # Emparejamos índice y valor comenzando desde el índice 5
print(emparejar(['a', 'b', 'c']))  # Lista de ejemplo


#------------------------------------------------------------------------------
from itertools import cycle

def emparejar(lista: list) -> list:
    return [(i, e) for i, e in zip(cycle([1, 2]), lista)]  # Emparejamos la secuencia cíclica con la lista
print(emparejar(['a', 'b', 'c', 'd']))  # Lista de ejemplo


for a, b  in zip([1,2,3,4,5,6,7,8,9], ['a', 'b', 'c','a', 'e', 'g', 'u', 'r']):
    print(a, b)
    """
    1 a
    2 b
    3 c
    4 a
    5 e
    6 g
    7 u
    8 r
    """

def parejas(filas, columnas):
    res = []
    for fila in range(filas):
        for columna in range(columnas):
            res.append((fila, columna))
    return res



print(parejas(2,3))
"""
print(2,3) = [ (0,0) , (0,1) , (0,2)
               (1,0) , (1,1) , (1,2)
               (2,0) , (2,1) , (2,2)
                                   ]
"""
#------------------------------------------------------------------------------

from random import randrange

bombo = list(range(100))

while len(bombo) > 0:
    i = randrange(len(bombo))
    n = bombo.pop(i)
    print(n, end=' ')


def histograma(s: str) -> dict[str, int]:
    """Devuelve el histograma de una cadena"""
    res = {}  
        else:  # Si no está en el diccionario, lo añadimos con frecuencia 1
            res[c] = 1
    return res  # Devolvemos el diccionario con las frecuencias

# Probamos la función con una cadena de ejemplo
print(histograma("Esto es una prueba de cadena de ejemplo"))

#------------------------------------------------------------------------------


def sobre(m,n):
    """ Calcula m sobre n """
    if m == 0 and n > 0:
        return 0
    if m >= 0 and n ==0:
        return 1
    return sobre(m-1, n - 1) + sobre(m - 1, n)

def factorial(n):
    res = 1
    while n >= 1:
        res *= n
        n-= 1
    return res



def sobre2(m ,n):
    return factorial(m) // (factorial(n) * factorial(m - n))



def sobre(m, n):
    """ Calcula m sobre n (Coeficiente Binomial) de manera recursiva """
    if m == 0 and n > 0:  # Si m es 0 y n es mayor que 0, no se puede elegir más elementos de los que hay
        return 0
    if m >= 0 and n == 0:  # Si n es 0, siempre hay una forma de elegir 0 elementos (C(m, 0) = 1)
        return 1
    # Fórmula recursiva: C(m, n) = C(m-1, n-1) + C(m-1, n)
    return sobre(m - 1, n - 1) + sobre(m - 1, n)

def factorial(n):
    """Calcula el factorial de n"""
    res = 1
    while n >= 1:# Inicializamos un diccionario vacío para almacenar las frecuencias
    for c in s:  # Recorremos cada carácter de la cadena
        if c in res:  # Si el carácter ya está en el diccionario, aumentamos su frecuencia
            res[c] += 1
        res *= n  # Multiplicamos res por cada número de n hasta llegar a 1
        n -= 1  # Disminuimos n en cada iteración
    return res

def sobre2(m, n):
    """Otra forma de calcular m sobre n utilizando la fórmula de factorial"""
    return factorial(m) // (factorial(n) * factorial(m - n))

def triangulo(filas) -> None:
    """Construye el triángulo de Pascal"""
    for m in range(filas):
        # Imprime espacios para centrar el triángulo
        print('  ' * (filas - m), end='')  
        
        for n in range(m + 1):
            # Imprime cada valor de m sobre n (coeficiente binomial)
            print(f"{sobre(m , n):3}", end=' ')
        
        # Salto de línea al final de cada fila
        print()

# Ejemplo de uso
triangulo(5)  # Llamada para generar un triángulo de 5 filas


#------------------------------------------------------------------------------
"""
Ejercicio de cuadrados
"""

def cuadrados(n: int) -> list[list[int]]:
# Devuelve un cuadrado n * n con los números del 1 al n*n.
    res = []  
    c = 1      # Comienza el contador en 1, que será el valor que se agregará a la matriz
    for i in range(n):  # Bucle exterior que se repite n veces, una por cada fila
        f = []  # Crea una lista vacía que representará una fila del cuadrado 
        for j in range(n):  # Bucle interior que se repite n veces, una por cada columna
            f.append(c)  # Agrega el valor actual de c a la fila
            c += 1        # Incrementa el valor de c para el siguiente número
        res.append(f)  # Después de completar una fila, se agrega a la lista de resultados
    return res  # Devuelve la lista res que contiene el cuadrado completo


def imprimir_cuadrado(c: list[list[int]]) -> None:
    """Imprime el cuadradro generado por la funcion cuadrado() """
    for fila in c:
        for e in fila:
            print(f"{e:3}", end=' ')
        print()
        

imprimir_cuadrado(cuadrado(7))

#------------------------------------------------------------------------------

from itertools import count  # Importa 'count' de itertools para generar números secuenciales

def cuadrado_magico(n: int):
    """Devuelve el cuadrado mágico de n * n"""
    
    # Inicializa una matriz de n x n con ceros. Usamos una lista por comprensión para evitar referencias compartidas.
    res = [[0] * n for _ in range(n)]  
    
    c = count(1)  # Crea un generador que produce números secuenciales comenzando desde 1
    fila, col = 0, n // 2  # Comienza en la primera fila y la columna central

    # Rellena la matriz con los números del 1 al n^2
    for _ in range(n * n):
        res[fila][col] = next(c)  # Coloca el siguiente número del generador en la posición actual
        
        # Calcula la siguiente fila y columna según las reglas del cuadrado mágico:
        # 1. La fila se mueve hacia arriba (decrementando), pero con el operador % se envuelve de nuevo
        #    al llegar al principio (fila = 0), para permitir un movimiento cíclico.
        # 2. La columna se mueve hacia la derecha (incrementando), y también se envuelve con % cuando
        #    se llega al final (col = n-1).
        nueva_fila, nueva_col = (fila - 1) % n, (col + 1) % n
        
        # Si la nueva posición ya está ocupada, movemos hacia abajo en lugar de hacia arriba
        if res[nueva_fila][nueva_col] != 0:
            nueva_fila, nueva_col = fila + 1, col  # Se mueve hacia abajo (fila + 1) y se mantiene la columna igual
        
        # Actualizamos la fila y columna con las nuevas posiciones calculadas
        fila, col = nueva_fila, nueva_col
    
    return res  # Devuelve la matriz que contiene el cuadrado mágico generado

#------------------------------------------------------------------------------




#EJERCICIO DE RACIONALES PARA 2 TRIMESTRE
"""
Modulo de representacion y manipulacion de úmeros racionales
"""

import math
#colocar las fotos que he realizado con el telefono
def racional(num:int, den:int):
    """Contruye un racional a partir de un numaración 
    y del denominador"""
    return(num, den)


def numerador(r):
    """Devuelve el numerador de una racional."""
    return['num']
def mult_rac(r1, r2):
    """Multiplicar dos racionales"""
    return(r1[0] * r2[0], r1[1] * r2[1])


def suma_recta(r1, r2):
    """Suma ds racionaes."""
    return(r1[0] * r2[1] + r1[1] * r2[0],r1[1] * r2[1])

def _simplificar(r):
    """Simplifica un numoer racional."""
    mcd = math.gcd(r[0], r[1])
    return (r[0] // mcd, r[1] // mcd)
    

#Modulo principal
import racionales
#sustituimos  racionales por el nombre del archivo
rac1 = (2, 3)
rac2 = (4, 5)

mult=  racionales.mult_rac(rac1, rac2)#se envia en forma de tupla
num, den = mult
print(f"{num}/{den}")
suma=  racionales.suma_recta(rac1, rac2)#se envia en forma de tupla
num, den = suma
print(f"{num}/{den}")
