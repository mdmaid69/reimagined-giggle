import math
def calculate_logarithm(base, x):
        return math.log(x, base)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)