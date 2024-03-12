# taller 1

1.Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).
-----------------------
[![image.png](https://i.postimg.cc/CxsRrGnw/image.png)](https://postimg.cc/dhDQLT9f)

2.Realice un programa que lea tres números reales y determine cuál es el mayor.
-----------------------
```python
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
```
3.Realice un programa que lea un número enteros y determine si es par o impar.
-----------------------
```python

```

4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
-----------------------
```python
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

```
5.Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
-----------------------
```python
na= input("Introduzca el primer número real ")
nb= input("Introduzca el segundo número real ")
nc= input("Introduzca el tercer número real ")
if (('-' in na) or ('.' in na)) or na.isdigit():
    a: float
    a=(float(na))   
    if (('-' in nb) or ('.' in nb))or nb.isdigit():
        b: float
        b=(float(nb))
        if (('-' in nc) or ('.' in nc))or nc.isdigit():  
            c: float
            c=(float(nc))  
            e:float 
            e=a+b
            if(e<c):
                print("la suma de", a, "y", b ," es menor que", c)
            elif (e>c):
                print("la suma de", a, "y", b ," es mayor que", c)
            else:
                print("la suma de", a, "y", b ," es igual a", c)
        else:
            print(" introduzca solo números reales")
    else:
        print(" introduzca solo números reales")
else:
    print(" introduzca solo números reales")

```
6.Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
-----------------------
```python
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
            
```
7.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
-----------------------
-El promedio
-La mediana
-El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
-Ordenar los números de forma ascendente
-Ordenar los números de forma descendente
-La potencia del mayor número elevado al menor número
-La raíz cúbica del menor número

```python


```
8.Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.
-----------------------
```python

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
        
```
9.Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.
-----------------------
```python
print("este programa le enseñará el nombre de la capital de los paises de América:")
P= input("Escriba un país de América(en minúsculas y con buena otrografía)"
         "para saber cual es su capital:")
match(P):
    case "antigua y barbuda":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: saint john's")
    case "argentina":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: buenos aires")
    case "bahamas":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: nasáu")
    case "barbados":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: bridgetown")
    case "belice":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: belmopán")
    case "bolivia":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: sucre")
    case "brasil":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: brasilia")
    case "canadá":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: ottawa")
    case "chile":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: santiago")
    case "colombia":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: bogotá")
    case "costa rica":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: san josé")
    case "cuba":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: la habana")
    case "dominica":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: roseau")
    case "ecuador":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: quito")
    case "el salvador":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: san salvador")
    case "estados unidos":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: washington d. c.")
    case "granada":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: saint george")
    case "guatemala":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: ciudad de guatemala")
    case "guyana":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: georgetown")
    case "haití":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: puerto príncipe")
    case "honduras":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: tegucigalpa")
    case "jamaica":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: kingston")
    case "méxico":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: ciudad de méxico")
    case "nicaragua":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: managua")
    case "panamá":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: ciudad de panamá")
    case "paraguay":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: asunción")
    case "perú":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: lima")
    case "república dominicana":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: santo domingo")
    case "san cristóbal y nieves":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: basseterre")
    case "san vicente y las granadinas":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: kingstown")
    case "santa lucía":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: castries")
    case "surinam":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: paramaribo")
    case "trinidad y tobago":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: puerto españa")
    case "uruguay":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: montevideo")
    case "venezuela":
        print("la capital del pais",'"',P,'"',"(en minúsculas) es: caracas")
    case _:
        print("Usted no ha introducido el nombre de ningún país de américa"
               " siguiendo las indicaciones dadas, por favor intente de nuevo.")
```
10.Escriba un programa que dada una distancia calcule:
-----------------------
-El tiempo que le tomaría a la luz recorrer la distancia.
-El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
-El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
-El tiempo que le tomaría a Bolt recorrer la distancia.
```python
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

``` 
