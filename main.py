n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)