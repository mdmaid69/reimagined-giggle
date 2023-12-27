import random
print(random.randint(0, 100))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)