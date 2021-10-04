x1=int(input("Elemento x del primer vector: "))
y1=int(input("Elemento y del primer vector: "))
x2=int(input("Elemento x del segundo vector: "))
y2=int(input("Elemento y del segundo vector: "))

def resta1 (x1,x2):
    return x2-x1
def resta2 (y1,y2):
    return y2-y1
x=x2-x1
y=y2-y1
def modulo(x,y):
   return (x**2+y**2)**(1/2)
print(modulo(x,y))

x3=x/modulo
y3=y/modulo

print('El resultado es ', x3 , y3 )