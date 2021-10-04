x1=int(input("Elemento x del primer vector: "))
y1=int(input("Elemento y del primer vector: "))
x2=int(input("Elemento x del segundo vector: "))
y2=int(input("Elemento y del segundo vector: "))

def resta1 (x1,x2):
    return x2-x1
def resta2 (y1,y2):
    return y2-y1


vector=(resta1(x1,x2),resta2(y1,y2))
print(vector)