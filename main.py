import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)