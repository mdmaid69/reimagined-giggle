import math
def calculate_combinations(n, k):
        return math.comb(n, k)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])