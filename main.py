import math
def calculate_permutations(n, k):
        return math.perm(n, k)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])