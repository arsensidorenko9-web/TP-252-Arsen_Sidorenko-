a = int(input("a = "))
b = int(input("b = "))
op =input("Яка операція? (+,-,*,/)")

def plu(a,b):
    return(a+b)
def min(a,b):
    return(a-b)
def mull(a,b):
    return(a*b)
def dil(a,b):
    if b==0:
       return ("На нуль ділити не можна")
    return(a/b)

if op=="+":
 res = plu(a,b) 
elif op=="-":
 res = min(a,b)
elif op=="*":
 res = mull(a,b)
elif op=="/":
 res = dil(a,b)
else: "Error"

print("Результат:",res)