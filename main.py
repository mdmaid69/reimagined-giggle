import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)