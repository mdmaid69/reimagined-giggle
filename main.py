n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)