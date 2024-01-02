numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)