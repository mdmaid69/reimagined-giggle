n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))