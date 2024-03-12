#Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

def checkfloat(numero):
    try:
        float(numero)
        return True
    except:
        return False

def longitud_de_onda(frecuencia):
    c = 3 * 10**8
    longitud_de_onda = c / frecuencia
    if longitud_de_onda < 1e-11:
        return "Rayos gamma"
    elif longitud_de_onda < 1e-8:
        return "Rayos X"
    elif longitud_de_onda < 4e-7:
        return "Espectro visible"
    elif longitud_de_onda < 7e-7:
        return "Ultravioleta"
    elif longitud_de_onda < 1e-3:
        return "Infrarrojo"
    else:
        return "Ondas de radio"

if __name__ == "__main__":
    frecuencia = float(input("Ingrese la frecuencia de la onda en Hz: "))
    if frecuencia < 0:
        print("La frecuencia no puede ser negativa")
        exit()
    elif checkfloat(frecuencia) == False:
        print("Error, los valores ingresados no son numeros")
        exit()
    else:
        print("La longitud de onda de la frecuencia ingresada se encuentra en el espectro: ", longitud_de_onda(frecuencia)) 
        
    
   





