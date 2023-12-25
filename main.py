import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def is_palindrome(s):
        return s == s[::-1]