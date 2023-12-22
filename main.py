import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))