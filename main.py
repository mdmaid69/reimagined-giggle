import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)