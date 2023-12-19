import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b