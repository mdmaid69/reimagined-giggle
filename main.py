import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)