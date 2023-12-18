def is_palindrome(s):
        return s == s[::-1]
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)