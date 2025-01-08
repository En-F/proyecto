# Supongamos que ya hemos cargado el XML y tenemos la raíz como 'raiz'
import xml.etree.ElementTree as ET

# Aquí 'raiz' es el nodo raíz del XML.
# Asumimos que ya hemos parseado el XML y tenemos la estructura cargada.
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

# Este código recorre todos los elementos hijos de la raíz.
for hija in raiz:
    # 'hija' es cada uno de los elementos hijos de 'raiz'.
    # Los elementos hijos de 'raiz' son: <alumno> y <madre>.
    
    # Accedemos al primer hijo de cada 'hija' (que es 'hija[0]')
    # 'hija[0]' es el primer subelemento dentro de cada 'alumno' o 'madre'.
    # En este caso, en un <alumno>, el primer hijo es <dni>.
    # En <madre>, el primer hijo también es <dni>.
    
    print(hija[0].text)  # Imprime el texto dentro de ese primer subelemento, que es el <dni> de cada 'alumno' o 'madre'.
