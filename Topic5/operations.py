import functions

a = int(input("a = "))
b = int(input("b = "))
op = input("Яка операція? (+,-,*,/) ")

if op == "+":
    res = functions.plu(a, b)
elif op == "-":
    res = functions.min(a, b)
elif op == "*":
    res = functions.mull(a, b)
elif op == "/":
    res = functions.dil(a, b)
else:
    res = "Error"
print("Результат:", res)
