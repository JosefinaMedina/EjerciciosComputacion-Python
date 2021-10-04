import math as m

a=int(input("Coeficiente cuadratico: "))
b=int(input("Coeficiente lineal: "))
c=int(input("Ordenada al origen: "))

if a==0:
    if b!=0:
        print (f"La raiz es {-c/b}")
    if b==0:
        if c!=0:
            print ("No existen raices")
        if c==0:
            print ("Todo el dominio es raiz")

if a!=0:
    x1=(-b-m.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b+m.sqrt(b**2-4*a*c))/(2*a)

    if m.sqrt(b**2-4*a*c)>0:
        print(f"Las raices son reales y son {x1} y {x2}")

    if m.sqrt(b**2-4*a*c)<0:
        print(f"Las raices son imaginarias y son {x1} y {x2}")

    if m.sqrt(b**2-4*a*c)==0:
        print(f"La raiz es unica y es {x1}")
