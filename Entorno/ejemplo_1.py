def comprueba_numero(mensaje):
    while (True):
        numero = int(input(mensaje))
        if numero>=0:
            return numero

par= comprueba_numero("Introduce un número entero par y positivo:  ")
impar = comprueba_numero("Introduce un número entero impar y positivo: ")
positivo=comprueba_numero("Introduce un número entero cualquiera y positivo: ")

suma=par + impar + positivo
print("La suma de los número es: " + str(suma))

#debido a la repeticion de codigo se ha llevadoa cabo la etraccion y 
# mediante el uso de variables con nombre mas explicativos se va llamando a funcion 