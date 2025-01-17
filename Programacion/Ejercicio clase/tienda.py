"""
Modulo principal de la tienda online
"""
from Cliente import cliente

cliente = ContenedorCliente()

cliente.meter_cliente(cliente("17283948B","Pepe","Romero Vargas",34))
cliente.meter_cliente(cliente("16273849K","Maria","Morales Mora",23))

pepe = cliente.buscar_cliente_por_dni("16273849K")
print(pepe.edad)


