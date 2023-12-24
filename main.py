import math
def calculate_exponential(x):
        return math.exp(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)