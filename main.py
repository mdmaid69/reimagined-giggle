import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))