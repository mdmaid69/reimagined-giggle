n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3