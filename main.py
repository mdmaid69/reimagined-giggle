n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)