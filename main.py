import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)