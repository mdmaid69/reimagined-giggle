import math
def calculate_arc_tangent(x):
        return math.atan(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)