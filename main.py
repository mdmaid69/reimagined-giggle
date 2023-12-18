import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)