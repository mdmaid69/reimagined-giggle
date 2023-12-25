import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)