import math

m1=int(input("Pendiente de la recta 1: "))
b1=int(input("Ordenada al origen de la recta 1: "))

m2=int(input("Pendiente de la recta 2: "))
b2=int(input("Ordenada al origen de la recta 2: "))

if m1!=m2:
    x=(b2-b1)/(m1-m2)
    print(f"El punto de interseccion es {x}")
if m1==m2:
    print(f"Las rectas no se intersecan")
