import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])