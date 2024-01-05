import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)