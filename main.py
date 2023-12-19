import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])