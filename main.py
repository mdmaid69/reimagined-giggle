import math
def calculate_ceiling(x):
        return math.ceil(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)