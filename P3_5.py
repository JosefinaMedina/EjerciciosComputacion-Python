import math
from math import factorial
import numpy as np

lista=[]
n=int(input("Cantidad de numeros que va a ingresar: "))
for i in range (0,n):
    ele=int(input("Ingrese el numero: "))
    lista.append(ele)

fac=[]
for i in lista:
    ele1=factorial(i)
    fac.append(ele1)
vector1=np.array(fac)
print(vector1)
    