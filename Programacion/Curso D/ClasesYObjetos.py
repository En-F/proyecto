class Celular: 
    def __init__(self, marca, modelo, camara):  
        self.__marca = marca 
        self.__modelo = modelo  
        self.__camara = camara 

    def llamar(self): 
        print(f'Estas haciendo un llamado desde un: {self.__modelo}') 
    
    def cortar(self): 
        print(f'Cortaste la llamada desde tu: {self.__modelo}') 

# Creación de objetos Celular
celular1 = Celular("Samsung", "S23", "48MP") 
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP") 

# Haciendo una llamada desde celular2
celular2.llamar()
celular1.llamar()
