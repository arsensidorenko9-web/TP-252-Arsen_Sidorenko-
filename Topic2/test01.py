import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def disk (a,b,c):
    return b**2-4*a*c
def kore (a,b,c):
    d = disk (a,b,c)

    if d > 0:
       x1 = (-b + math.sqrt(d)) / (2*a)
       x2 = (-b - math.sqrt(d)) / (2*a)
       print ("Має два корені", x1,x2)
    elif d == 0:
        x= -b / (2*a)
        print(x,"Має один корінь")
    else:
        print("Коренів немає")
(kore(a,b,c))

