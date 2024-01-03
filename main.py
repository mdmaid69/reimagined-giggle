import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def is_palindrome(s):
        return s == s[::-1]