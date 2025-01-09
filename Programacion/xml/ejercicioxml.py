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


# Utilizamos findall para encontrar todos los elementos <alumno> dentro del XML
for alumno in raiz.findall('alumno'):
    # Para cada elemento <alumno>, encontramos el primer subelemento <dni>
    # y luego obtenemos el texto de ese elemento <dni>
    print(alumno.find('dni').text)  # Imprime el texto dentro del <dni> (el número de DNI)


alumno = raiz.find('alumno')  # Encuentra el primer <alumno>
numero = alumno.get('numero')  # Obtiene el valor del atributo 'numero'
numero = alumno.attrib['numero'] # Usamos [] para acceder al atributo 'numero'
print(numero)  # Imprime '111'


for alumno in raiz.findall('alumno'):
    numero = alumno.get('numero')  # Obtiene el valor del atributo 'numero' del <alumno>
    dni = alumno.find('dni').text  # Obtiene el texto del  nodo hijo <dni> dentro del nodo <alumno>
    print(numero, dni)  # Imprime el número (atributo 'numero') y el DNI


# Imprimimos la estructura completa del árbol XML
ET.dump(raiz)


# Recorremos todos los elementos <nota> que aparecen en el árbol XML, sin importar su nivel de anidamiento.
for nota in raiz.iter('nota'):
    # Convertimos el valor de texto de <nota> a entero, le sumamos 1 y luego lo asignamos a la variable nueva_nota.
    nueva_nota = int(nota.text) + 1
    
    # Asignamos el nuevo valor de nueva_nota al elemento <nota> en formato de texto.
    nota.text = str(nueva_nota)
    
    # Establecemos un atributo 'modificado' con valor 'si' para marcar que este nodo ha sido modificado.
    nota.set('modificado', 'si')

# Guardamos los cambios realizados en el árbol XML en un nuevo archivo llamado 'salida.xml'.
arbol.write('salida.xml',encoding='utf-8', xml_declaration=True)


#Modifica añadiendo un nombre a la etiqueta propio de nombre.
import xml.etree.ElementTree as ET

arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

# Recorremos todos los elementos <alumno> dentro del árbol XML.
for alumno in raiz.findall('alumno'):
    # Dentro de cada <alumno>, buscamos el subelemento <nota>.
    nota = alumno.find('nota')

    # Convertimos el valor de la <nota> a entero, le sumamos 1, y lo almacenamos en 'nueva_nota'.
    nueva_nota = int(nota.text) + 1

    # Actualizamos el contenido de texto de la <nota> con el nuevo valor (nueva_nota).
    nota.text = str(nueva_nota)

    # Establecemos un atributo 'modificado' con valor 'si' en el elemento <nota>.
    nota.set('modificado', 'si')

    # Buscamos el subelemento <nombre> dentro de <alumno> y luego buscamos su subelemento <propio>.
    nombre = alumno.find('nombre/propio')

    # Modificamos el valor de <propio> agregando la palabra ' María' al final del texto original.
    nombre.text = nombre.text + ' María'

# Guardamos el árbol XML modificado en un nuevo archivo llamado 'salida.xml'.
# El archivo se guarda con codificación UTF-8 y se incluye una declaración XML en el encabezado.
arbol.write('salida.xml', encoding='utf-8', xml_declaration=True)
