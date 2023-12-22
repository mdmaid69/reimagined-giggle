import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)