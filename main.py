def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)