import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b