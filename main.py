import math
def calculate_sign(x):
        return math.copysign(1, x)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b