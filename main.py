n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)