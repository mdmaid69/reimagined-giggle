n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Cube numbers:", [x**3 for x in range(n)])