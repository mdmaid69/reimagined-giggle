import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])