import math
def calculate_combinations(n, k):
        return math.comb(n, k)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])