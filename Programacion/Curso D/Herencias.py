


class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def descripcion_datos(self):
        print(f"El nombre es {self.nombre} y su edad es {self.edad}")   

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def descripcion_grado(self):
        print(f"El grado de {self.nombre} es {self.grado}")
    


estudiante_1= Estudiante("Enrique",24,4)
estudiante_1.descripcion_datos()
estudiante_1.descripcion_grado()