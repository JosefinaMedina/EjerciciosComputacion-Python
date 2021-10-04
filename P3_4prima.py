import math
n=int(input("La cantidad de numeros triangulares es: "))
t=1
m=1
while t<=n:
    m=t*(t+1)/2
    t=t+1
    print(m)
