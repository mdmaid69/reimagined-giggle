import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])