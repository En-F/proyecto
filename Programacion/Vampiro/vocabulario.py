"""
El vocabulario del juego
"""
class Categoria:
    """
    La categoría de las palabras del vocabulario.
    """
    
verbo = Categoria()
nombre = Categoria()    

class Palabra:
    """
    Las palabras que entiende  el juego 
    """
    def __init__(self, lexema:str, categoria:Categoria):
        self.__lexema = lexema
        self.__categoria = categoria
        
    def lexema(self):
        """Devuelve  el elxemade la palabra"""
        return self.__lexema
    
    def categoria(self):
        """Devuelve la categoria de la palabra"""
        return self.__categoria

verbo = Categoria()
nombre = Categoria() 

norte = Palabra(["norte","n"],verbo)
sur = Palabra(["sur","s"],verbo)
palanca = Palabra (["palanca"],nombre)
fin = Palabra(["fin","acabar","terminar","finalizar"], verbo)


vocabulario = Vocabulario()
vocabulario.insertar([norte,sur,palanca,fin])


class Vocabulario:
    """El vocabulario de la aventura"""
    def __init__(self):
        self.palabra:dict[str, Palabra] = {}
        
    def insertar(self,palabra: Palabra):
        """Inserta una palabra en el  vocabulario."""
        for lexema in palabra.lexema():
            self.__palabras[lexema] = palabra
    
    def 
        
    
    