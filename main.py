from collections import Counter
print(Counter("hello world"))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)