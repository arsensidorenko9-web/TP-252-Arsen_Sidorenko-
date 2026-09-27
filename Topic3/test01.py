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

while True:
    a = input("a = ")
    if a == "Стоп":
        break
    a = int(a)

    b = input("b = ")
    if b == "Стоп":
        break
    b = int(b)

    op = input("Яка операція? (+,-,*,/)")
    if op == "Стоп":
        break

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