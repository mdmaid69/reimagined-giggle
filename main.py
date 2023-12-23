import math
def calculate_absolute_value(x):
        return math.fabs(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)