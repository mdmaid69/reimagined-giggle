import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)