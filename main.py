numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)