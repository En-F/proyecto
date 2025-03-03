"""
El odulo principal del juego vampiro
"""

from mapa import Lugar
from jugardor import Jugador
import vocabulario as v

vestibulo = Lugar("VESTIBULO", "Estas en el vestibulo del castillo...")
pasillo = Lugar("PASILLO","Estas en el pasillo principal  del castillo")
jugador =  Jugador(vestibulo)

lugar = jugador.lugar()
lugar.describir() 

while True:
    entrada = input("¿Que haces ahora?\n>")
    palabras = entrada.split()
    if len(palabras) == 0 :
        continue
    elif len(palabras) < 2:
        print("No  entiendo lo que dices.")
        continue
    
    verbo = v.vocabulario.Buscar(palabras[0])
    if verbo is None or verbo.categoria() != v.cat_verbo:
        print("No entiendo lo que dices")
        continue
    if len(palabras) == 2:
        nombre = v.vocabulario.Buscar(palabras[1])
        if nombre is not None and  nombre.categoria() != v.cat_nombre:
            print("No entiendo lo que dices")
            continue    
    
    if verbo == v.fin:
        print("Adios")
        break
    elif verbo == n.norte:
        salida = m.mapa.saldida_hacia(lugar,v.norte)
        if salida is None:
            print("No hay salida en esa direccion")
        else:
            lugar = salida
            lugar.describir()        
    elif verbo == n.sur:
        salida = m.mapa.saldida_hacia(lugar,v.sur)
        if salida is None:
            print("No hay salida en esa direccion")
        else:
            lugar = salida
            lugar.describir()    
        
        
    if  entrada ==v.fin.lexema()s:
        print("Adios")
        break
    elif entrada == v.norte.lexema():
        #Buscar salidas al norte desde el lugar actual 
        ...
    else:
        print("No entiendo lo que dices.")
     
        

