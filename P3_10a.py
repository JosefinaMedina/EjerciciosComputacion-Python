import math

a=int(input("Coeficiente cuadratico: "))
b=int(input("Coeficiente lineal: "))
c=int(input("Ordenada al origen: "))


if a==0:
    print("Es una funcion lineal")
if a!=0:
    x=-b/(2*a)
    y= a*x**2+b*x+c
    if x==-0:
         x=0
    if a>0:
        print(f"El minimo es {y} y esta en {x}")
    if a<0:
        print(f"El maximo es {y} y esta en {x}")
