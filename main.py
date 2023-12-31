import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)