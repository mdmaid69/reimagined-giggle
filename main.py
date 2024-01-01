import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))