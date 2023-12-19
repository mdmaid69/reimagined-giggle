import math
def calculate_sign(x):
        return math.copysign(1, x)
def is_palindrome(s):
        return s == s[::-1]