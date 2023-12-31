n = 10
print("Powers of 2:", [2**x for x in range(n)])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)