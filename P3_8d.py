#Escribir una función que reciba un vector al origen 
#(definido por sus puntos x, y) y devuelva un vector 
#equivalente, normalizado (debe devolver un
#par de valores)
import math

x=int(input("Elemento x del vector: "))
y=int(input("Elemento y del vector: "))

def modulo(x,y):
   return math.sqrt(x**2+y**2)

x1=x/modulo
y1=y/modulo

print('El resultado es ', x1,y1)