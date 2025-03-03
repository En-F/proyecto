"""Moddulo que implementa al jugar  de la aventura"""

from mapa import Lugar
class Jugador:
    """El Jugador """
    def __init__(self, inicial:Lugar ,):
        self.__Lugar = inicial  
    
    def lugar(self):
        """El lugar actual del jugador"""
        return self.__lugar
    
    def mover(self, nuevo:Lugar) -> None:
        """Mueve al jugador al nuevo lugar."""
        self.__Lugar = nuevo
        
        
        