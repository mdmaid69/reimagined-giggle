import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b