def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height