import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])