import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)