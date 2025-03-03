"""Modulo de classes relacionadas co el mapa del juego"""

import vocabulario as v
class Lugar:
    """Un lugar del juego"""
    def __init__(self,nombre:str ,descripcion:str):
        self.__nombre = nombre
        self.__descripcion = descripcion
    
    def nombre(self):
        """El nombre de un lugar"""
        return self.__nombre

    def descripcion(self):
        """La descripcion de un lugar"""
        return self.__descripcion    
    
    def describir(self):
        """Describe el lugar."""
        print(self.nombre())
        print(self.descripcion())
    


class Mapa:
    """
    El mapa del juego 
    """
    def __init__(self):
        self.mapeado = {}
    
    def insertar(self, lugar:Lugar, conexiones: dict):
        """Me mete en el mapa un lugar con sus conecxiones"""   
        self.__mapeado[lugar] = conexiones
    
    def conexiones(self,lugar:Lugar):
        return self.__mapeado[lugar]


    def saldida_hacia(self, lugar:Lugar, direccion: v.Palabra) -> Lugar|None:
        """ Que salida hay desde un lugar hacia una direccion 
        Devuelve None si no hay salidas hacia esta direccion
        """
        return self.__mapeado[lugar][direccion] 
    
"""    
{
    vestibulo:{
        norte:pasillo}
     },
    pasillo:{
        sur:vestibulo
    }
}
"""

vestibulo = Lugar("VESTIBULO", "Estas en el vestibulo del castillo...")
pasillo = Lugar("PASILLO","Estas en el pasillo principal  del castillo")
mapa = Mapa()
mapa.inserta(vestibulo,{v.norte: pasillo})
mapa.inserta(vestibulo,{v.sur: vestibulo})