import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])