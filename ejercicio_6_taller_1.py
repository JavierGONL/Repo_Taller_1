#Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

if __name__ == '__main__':
    letra = input("Ingrese una letra: ")
    
    if len(letra) > 1:
        letra = input("ingrese solo letras: ")  
    elif letra.isalpha == False:
        letra = input("ingrese solo letras(A-Z sin acento): ")
    else:
        if ord(letra) ==  (65 or 69 or 73 or 79 or 85 or 97 or 101 or 105 or 111 or 117):
            print("Es una vocal")
        else:
            print("Es una consonante")
            