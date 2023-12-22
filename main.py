import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)