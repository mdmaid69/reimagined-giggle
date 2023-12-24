import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True