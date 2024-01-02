import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b