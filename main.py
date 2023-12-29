import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b