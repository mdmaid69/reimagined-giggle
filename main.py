import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)