import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
print("Square numbers:", [x**2 for x in range(n)])