import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])