import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b