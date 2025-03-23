class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre= nombre
        self.apellidos = apellidos
        self.edad = edad

    def camina(self):
        print(f"{self.nombre} + está caminando")

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad

persona_1 = Persona("Mike", "Mendiola", 25)
persona_1.camina()


print(persona_1.get_nombre())
print(persona_1.get_edad())



#Hemos cambiado el nombre de la variable temporal para que se entienda mejor para el lector del codigo
#tambien hemos creado  dos geters que nos da acceso tanto al nombre como la edad, para que sea mas sencillo
