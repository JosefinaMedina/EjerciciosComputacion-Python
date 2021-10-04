import math
Numero1=int(input("El primer numero es: "))
Numero2=int(input("El segundo numero es: "))
if Numero1%2 != 0:
    Numero1= Numero1+1
else:
    Numero1=Numero1

while Numero1<(Numero2-1):
    Numero1=Numero1+2
    print(Numero1)

    
