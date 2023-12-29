import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])