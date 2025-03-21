positivo = False
while (not positivo):
    m = int(input("Introduce un número entero par y positivo: "))
    if m>=0:
        positivo= True

positivo = False

while (not positivo):
    n = int(input("Introduce un número entero impar y positivo: "))
    if n>=0:
        positivo= True

positivo = False

while (not positivo):
    p = int(input("Introduce un número entero cualquiera y positivo: "))
    if p>=0:
        positivo= True

suma=m+n+p
print("La suma de los número es: " + str(suma))