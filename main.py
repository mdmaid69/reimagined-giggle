n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)