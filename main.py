import math
def calculate_arc_cosine(x):
        return math.acos(x)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)