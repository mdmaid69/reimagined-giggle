import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b