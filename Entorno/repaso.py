class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No hay suficiente saldo para realizar el retiro")
        else:
            self.saldo = self.saldo - cantidad

    def ver_saldo(self):
        print("Saldo actual: ", self.saldo)

    def transferir(self, cantidad, cuenta_destino):
        if cantidad > self.saldo:
            print("No se puede transferir. Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            cuenta_destino.depositar(cantidad)
            print(f"Se ha transferido {cantidad} a la cuenta destino.")
            
# Crear una cuenta
cuenta1 = CuentaBancaria(1000)

# Depositar dinero
cuenta1.depositar(500)

# Ver saldo
cuenta1.ver_saldo()

# Retirar dinero
cuenta1.retirar(300)

# Ver saldo después del retiro
cuenta1.ver_saldo()

# Crear otra cuenta para transferir dinero
cuenta2 = CuentaBancaria(500)

# Transferir dinero entre cuentas
cuenta1.transferir(200, cuenta2)

# Ver los saldos después de la transferencia
cuenta1.ver_saldo()
cuenta2.ver_saldo()
#----------------------------------------------------------------------------


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aplicar_descuento(self, porcentaje_descuento):
        descuento = self.precio * porcentaje_descuento / 100
        self.precio = self.precio - descuento

    def aumentar_stock(self, cantidad_extra):
        self.cantidad += cantidad_extra

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad:
            print(f"No hay suficiente stock para vender {cantidad_vendida} unidades de {self.nombre}.")
        else:
            self.cantidad -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de {self.nombre}.")
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad}")
    

# Crear un producto
producto_1 = Producto("Camiseta", 20.0, 50)

# Aplicar un descuento
producto_1.aplicar_descuento(10)

# Aumentar stock
producto_1.aumentar_stock(30)

# Vender producto
producto_1.vender(10)

# Mostrar información del producto
producto_1.mostrar_info()

#---------------------------------------------------------------------

class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def viajar(self, distancia):
        self.kilometraje += distancia

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje} km")
    
    def obtener_edad(self):
        return 2025 - self.anio  # Año actual 2025

# Crear un vehículo
vehiculo_1 = Vehiculo("Toyota", "Corolla", 2015)

# Viajar con el vehículo
vehiculo_1.viajar(100)

# Mostrar la información del vehículo
vehiculo_1.mostrar_info()

# Mostrar la edad del vehículo
print(f"La edad del vehículo es: {vehiculo_1.obtener_edad()} años.")

#---------------------------------------------------------------------

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def aprobar(self):
        if self.promedio() >= 6:
            print(f"{self.nombre} ha aprobado con un promedio de {self.promedio():.2f}.")
        else:
            print(f"{self.nombre} no ha aprobado. Promedio: {self.promedio():.2f}.")

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio():.2f}")

# Crear un estudiante
estudiante_1 = Estudiante("Juan", 20, [7, 8, 6, 5])

# Mostrar la información del estudiante
estudiante_1.mostrar_info()

# Comprobar si ha aprobado
estudiante_1.aprobar()
