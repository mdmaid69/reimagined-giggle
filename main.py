import math
def calculate_permutations(n, k):
        return math.perm(n, k)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b