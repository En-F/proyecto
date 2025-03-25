def decorar(funcion):
    """Llama a una funcion la cual se le ha pasado como parametro"""
    def funcion_modificada():
        """Esto es una funcion dentro de otra funcion, esta siendo decorada por la funcion principal"""
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada


@decorar
#Puedes agregarlo antes o despues de ejecutar la funcion_modificada 
def saludo():
    print("Hola Enrique ")

saludo()