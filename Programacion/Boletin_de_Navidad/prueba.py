password = input("Introduce la contraseña:")

while True:
    intento = input("Introduzla la  palabras:")
    for i,e in enumerate(password):
        if i >= len(intento):
            print("*", end='')          
        elif intento[i] != e:   #no coincide
            print("*", end='')
        elif intento[i] == e :
            print(e, end='')
    print()
    if intento == password:
        break