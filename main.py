n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b