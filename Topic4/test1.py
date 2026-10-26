
def getNumber():
    while True:
        try:
            return float(input("Введіть число: "))
        except ValueError:
            print("Помилка")

def getOperation():
    while True:
        try:
            op = input("Введіть операцію (+, -, *, /): ")
            if op not in ["+", "-", "*", "/"]:
                raise ValueError
            return op
        except ValueError:
            print("ERROR")

def main():
    while True:
        op = getOperation()
        a = getNumber()
        b = getNumber()

        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            try:
             print(a / b)
            except ZeroDivisionError:
             print("На нуль ділити не можна!")


main()