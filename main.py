import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])