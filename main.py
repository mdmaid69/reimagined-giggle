import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b