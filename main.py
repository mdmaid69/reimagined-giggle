import math
def calculate_absolute_value(x):
        return math.fabs(x)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b