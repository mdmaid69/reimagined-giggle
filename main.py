import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])