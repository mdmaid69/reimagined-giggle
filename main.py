import math
def calculate_logarithm(base, x):
        return math.log(x, base)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])