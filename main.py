import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)