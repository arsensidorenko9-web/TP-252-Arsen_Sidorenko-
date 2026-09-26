a = int(input("a = "))
b = int(input("b = "))


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
match input("Яка операція? (+,-,*,/)"):
 case "+":
  res = plu(a,b) 
 case "-":
  res = min(a,b)
 case "*":
  res = mull(a,b)
 case "/":
  res = dil(a,b)
 case _:
  res = "Error"
print("Результат:",res)
