def find_difference(list1, list2):
        return set(list1) - set(list2)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)