import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))