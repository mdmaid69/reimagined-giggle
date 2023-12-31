import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)