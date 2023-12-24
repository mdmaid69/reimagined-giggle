n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])