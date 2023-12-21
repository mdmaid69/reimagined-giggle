import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])