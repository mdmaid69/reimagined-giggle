import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))