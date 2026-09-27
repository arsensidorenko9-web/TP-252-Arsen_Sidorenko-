numbers = [3, 1, 4]
print("Початковий:", numbers)

numbers.append(5)
print("append:", numbers)

numbers.extend([9, 2])
print("extend:", numbers)

numbers.insert(2, 77)
print("insert:", numbers)

numbers.remove(77)
print("remove:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)


numcopy = numbers.copy()
print("Скопійований список:", numcopy)


numbers.clear()
print("після clear:", numbers)

