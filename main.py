import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))