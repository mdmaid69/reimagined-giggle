import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)