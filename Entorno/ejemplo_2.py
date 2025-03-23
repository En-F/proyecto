        
def solicitar_datos():
    dolares = float(input ("Cuantos dolares: "))
    interes = float(input ("Cuanto interes: "))
    años = int(input ("Cantidad de años: "))
    return dolares,interes,años

def calcular_resultado():
    return dolares * ((1 + interes/100) **cant_anos)

dolares,interes,años = solicitar_datos()


def hacer_calculo():
    dolares,interes,años = solicitar_datos()
    print(f"En esta ocasión obtienes{calcular_resultado(dolares,interes,años)} dolares")
    if input("¿Quieres realizar el calculo de nuveo(s/n)") == s:
        hacer_calculo()
    
    
hacer_calculo()
