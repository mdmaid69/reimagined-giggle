n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)