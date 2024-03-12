#Escriba un programa que dada una distancia calcule:

#El tiempo que le tomaría a la luz recorrer la distancia.
#El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
#El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
#El tiempo que le tomaría a Bolt recorrer la distancia.

#La distancia que recorre la luz en un segundo es de 299 792 458 m/s.
#La distancia que recorre el sonido en un segundo es de 343 metros.
#El vehiculo comercial más veloz Bugatti Chiron Super Sport 300+ ( 136 m/s)
#Bolt recorre 100 metros en 9.58 segundos mas o menos 10.43 m/s.

def checkfloat(numero):
    try:
        float(numero)
        return True
    except:
        return False

if __name__ == "__main__":

    distancia = float(input("Ingrese una distancia en metros: ")) # D = v * t -> t = D / v
    if distancia < 0:
        print("La distancia no puede ser negativa")
        exit()
    elif checkfloat(distancia) == False:
        print("Error, los valores ingresados no son numeros")
        exit()
    else:
        tiempoLuz = distancia / 299792458
        print("el tiempo que tarda en recorer la distancia la luz es: ", tiempoLuz, "segundos")
        tiempoSonido = distancia / 343
        print("el tiempo que tarda en recorer la distancia el sonido es: ", tiempoSonido, "segundos")
        tiempoCarroMasVeloz = distancia / 136
        print("el tiempo que tarda en recorer la distancia el carro mas veloz es: ", tiempoCarroMasVeloz, "segundos")
        tiempoBolt = distancia / 10.43
        print("el tiempo que tarda en recorer la distancia Usain Bolt es: ", tiempoBolt, "segundos")