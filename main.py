import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])