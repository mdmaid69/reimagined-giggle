import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def is_palindrome(s):
        return s == s[::-1]