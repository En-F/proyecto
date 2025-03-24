class Estudiante:
    def __init__(self, nombre ,edad ,curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    def estudiar(self):
        print("Esta estudiando...")

    def dejar_estudiar(self):
        print("Ha parado de estudiar")

    def Leer(self):
        print("Esta leyendo un libro")  

nombre = input("Dime tu nombre: ")
edad = int(input("Dame tu edad: "))
curso = int(input("En que curso estas: "))

estudiante = Estudiante(nombre,edad,curso) 
print(f"""
    DATOS DEL ESTUDIANTE:\n\n
    Nombre :  {estudiante.nombre}\n
    Edad : {estudiante.edad}\n
    curso : {estudiante.curso}\n
    """)


while True:
    print("""
        ¿Qué quieres que haga el estudiante?\n\n
        Leer : 1\n
        Estudiar : 2\n
        Para de estudiar : 3\n
        Salir : 0
    """)
    opcion = input()
    if opcion.lower() == "1":
        estudiante.Leer() 
    elif opcion.lower() == "2":
        estudiante.estudiar()
    elif opcion.lower() == "3":
        estudiante.dejar_estudiar()
    elif opcion.lower() == "0":
        break