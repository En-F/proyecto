# class Circulo:
#     def __init__(self, radio):
#         self.__radio = radio

#     def __cuadrado(self, n):
#         return n ** 2

#     def area(self):
#         a = 3.141592 * self.__cuadrado(self.__radio)
#         return a

#     def valorRadio(self):
#         return self.__radio

#     def fijaRadio(self, nuevoRadio):
#         self.__radio = nuevoRadio

# radio = float(input("Por favor introduce el radio: "))
# c1 = Circulo(radio)
# area1 = c1.area()

# if area1 > 5:
#     print("Área mayor que 5")

# perímetro = 3.141592 * radio

# if perímetro > 10:
#     print("Perímetro mayor que 10")


class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    def area(self):
        return  3.141592 * (self.__radio ** 2)

    def set_radio(self):
        self.__radio = nuevoRadio

    def get_radio(self, nuevoRadio):
        self.__radio = nuevoRadio

    def perímetro(self):
        return 2 * 3.141592 * (self.__radio)

radio = float(input("Por favor introduce el radio: "))
circulo_1 = Circulo(radio)
area_1 = circulo_1.area()
perimetro_1= circulo_1.perímetro()

if area_1 > 5:
    print("Área mayor que 5")

if perimetro_1 > 10:
    print("Perímetro mayor que 10")
    

#hamos introducido unos seterrs y unos getters para usar mejor las variables ,
#tambien  hemos añadido el método perimetro que nos calcula el primetro de manera correcta
#He adecuado el nombre de las varibles temporales para que sean mas practica a la hora de entender el codigo 
