n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
print([x**2 for x in range(10)])