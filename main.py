import math
def calculate_permutations(n, k):
        return math.perm(n, k)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)