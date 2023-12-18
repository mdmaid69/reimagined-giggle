import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)