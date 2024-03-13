
a:float= float(input("(numero1)a:"))
b:float= float(input("(numero1)b:"))
c:float= float(input("(numero1)c:"))
d:float= float(input("(numero1)d:"))
e:float= float(input("(numero1)e:"))

ordenado={a,b,c,d,e}
longitud=sorted(ordenado)
index= len(longitud)//2
media=(a+b+c+d+e)/5

if len(ordenado) % 2 != 0:
        print("la mediana es "+ str(longitud[index]))
promedio_multiplicativo=(a*b*c*d*e)**0.2

lista_inversa=sorted(ordenado,reverse=True)

M:float=max(ordenado)
m:float=min(ordenado)
potencia1=M**m
raiz1=m**0.33333333333333333333333333333333
print("la media es "+ str(media))
print("el promedio multiplicativo es "+ str(promedio_multiplicativo))
print(str(longitud)+ "(el conjunto en orden ascendente)")
print(str(lista_inversa) +"(el conjunto en orden descendente)")
print("la potencia numero menor del numero mayor es " +str(potencia1))
print("raiz cubica del numero menor " + str(raiz1))