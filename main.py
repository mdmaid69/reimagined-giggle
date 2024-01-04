n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])