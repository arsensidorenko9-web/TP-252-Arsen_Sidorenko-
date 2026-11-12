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
def log(a, b, op, res):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{a} {op} {b} = {res}\n")