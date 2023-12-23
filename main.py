n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])