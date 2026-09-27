a = [1, 3, 5, 7, 9]

def find_pos(x):
    for i in range(len(a)):
        if a[i] >= x:
            return i
    return len(a)

x = 10

pos = find_pos(x)
a.insert(pos, x)

print(a)
