text = "Hello, world!"
print("Words:", len(text.split()))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)