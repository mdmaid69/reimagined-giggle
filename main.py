def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)