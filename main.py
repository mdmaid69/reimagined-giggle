import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def count_elements(lst):
        return len(lst)