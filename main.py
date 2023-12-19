import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)