
import xml.etree.ElementTree as ET
arbol = ET.parse('ejemplo.xml')
libros = arbol.getroot()

for libro in libros:
    print(libro.tag, libro.attrib)