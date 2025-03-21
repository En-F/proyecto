dolares = input ("Cuantos dolares: ")
interes = input ("Cuanto interes: ")
interes = float(interes)
annos = input ("Cantidad de años: ")
annos = int(annos)
print ""
resultado = dolares * ((1 + interes/100) **cant_anos)
print "En esta ocasión obtienes”, resultado, “dólares”
dolares = input ("Cuantos dólares quieres ahora?: ")
interes = float(interes)
annos = input ("Cantidad de años: ")
annos = int(annos)
print "En este segundo cálculo obtienes”, resultado, “dólares”