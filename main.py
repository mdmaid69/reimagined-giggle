import itertools
print(list(itertools.permutations([1, 2, 3])))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)