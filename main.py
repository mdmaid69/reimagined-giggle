import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)