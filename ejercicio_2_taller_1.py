#Realice un programa que lea tres números reales y determine cuál es el mayor.

def checkfloat(numero):
    try:
        float(numero)
        return True
    except:
        return False

if __name__ == "__main__":

        
        numero1 = input("Ingrese el primer número: ")
        numero2 = input("Ingrese el segundo número: ")
        numero3 = input("Ingrese el tercer número: ")
        if checkfloat(numero1) == False or checkfloat(numero2) == False or checkfloat(numero3) == False:
            print("Error, los valores ingresados no son numeros")
            exit()
        else:
            numero1 = float(numero1)
            numero2 = float(numero2)
            numero3 = float(numero3)

        if numero1 > numero2 and numero1 > numero3:
            print("El primer numero es el mayor")
        elif numero2 > numero1 and numero2 > numero3:    
            print("El segundo numero es el mayor")
        elif numero3 > numero1 and numero3 > numero2:
         print("El tercer numero es el mayor")
        else:
            if numero1 == numero2 and numero1 == numero3:
                print("Hay un empate entre los tres numeros")
            elif numero1 == numero2:
                print("Hay un empate entre el primer y segundo numero")
            else:
                print("Hay un empate entre el primer y tercer numero")