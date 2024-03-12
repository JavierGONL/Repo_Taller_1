#Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo

def checkfloat(numero):
    try:
        float(numero)
        return True
    except:
        return False

if __name__ == "__main__":
    
    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    if checkfloat(numero1) == False or checkfloat(numero2) == False:
        print("Error, los valores ingresados no son numeros")
        exit()
    else: 
        numero1 = float(numero1)
        numero2 = float(numero2)

    if numero1 % numero2 == 0:
        print("El numero es multiplo del segundo numero")
    else:
        print("El primer numero no es multiplo del segundo numero")
