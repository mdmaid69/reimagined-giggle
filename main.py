import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b