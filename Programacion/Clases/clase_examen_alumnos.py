class Alumno:
    def __init__(self,nombre,grupo):
        self.__set_nombre(nombre)
        self.__set_grupo(grupo)
        self.__asignatura = {}

    def __set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __set_grupo(self,grupo):
        self.__grupo = None

    def get_grupo(self):
        return self.__grupo


class Grupo:
    """Creamos la clase grupo"""
    def __init__(self, nombre):
        self.nombre = nombre  
        self.alumnos = []  

    def añadir_alumno(self,alumno):
        self.alumnos.append(alumno)
        alumno.grupo = self





class Asignatura:
    
    def __init__(self,denominacion, trimestre):
        self.__set_denominacion = denominacion
        self.__set_trimestre = trimestre
        self.alumnos = []

    def __set_denominacion(self,denominacion):
        self.__denominacion = denominacion

    def __set_trimestre(self,trimestre):
        self.__trimestre = trimestre
    
    def matricular_alumno(self,alumno):
        """Matricular a un alumno a una asignatura"""
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
        return self





Alumno_1 = Alumno("Manuel")
print(Alumno_1.get_nombre())