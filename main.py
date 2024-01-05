import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)