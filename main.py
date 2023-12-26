import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)