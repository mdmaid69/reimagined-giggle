for i in range(10): print(i)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)