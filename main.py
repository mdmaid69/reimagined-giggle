numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)