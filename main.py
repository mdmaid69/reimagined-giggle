n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height