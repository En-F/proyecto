"""
Modulo de gestion de clientes.
"""

class cliente:
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


class ContenedorCliente:
    def __init__(self):
        self.contenedor = {}
    
    def meter_cliente(self, c:cliente):
        """Mete un cliente en el contenedor"""
        self.contenedor[c.dni] = c
        
    def sacar_cliente(self, c:str):
        """Saca el cliente de un contenedor """
        del self.contenedor[c.dni]                   
    
    def sacar_cliente_por_dni(self, dni:str):
        """Saca el cliente de un contenedor conociendo su dni"""
        del self.contenedor[dni]                   
    
    def buscar_cliente_por_dni(self, dni:str):
        """Busca el ciente dentro del contenedor por su DNI, 
        y luego lo devuelve si existe"""
        return self.contenedor[dni]
    
    