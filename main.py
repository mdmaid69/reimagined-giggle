n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)