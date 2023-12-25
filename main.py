import math
def calculate_error_function(x):
        return math.erf(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)