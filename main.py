import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
i = 0
while i < 5:
        print(i)
        i += 1