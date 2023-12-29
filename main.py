import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))