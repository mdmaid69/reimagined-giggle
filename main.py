import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def remove_duplicates(lst):
        return list(set(lst))