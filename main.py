n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))